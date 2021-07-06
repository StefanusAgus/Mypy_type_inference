import ast
from astunparse import unparse
from mypy.main import *
from mypy.nodes import CallExpr, NameExpr


def get_type_dict(script_path: Optional[str],
         stdout: TextIO,
         stderr: TextIO,
         args: Optional[List[str]] = None, *, filepath: str
         ):
    """Main entry point to the type checker.
    Args:
        script_path: Path to the 'mypy' script (used for finding data files).
        args: Custom command-line arguments.  If not given, sys.argv[1:] will
        be used.
    """
    util.check_python_version('mypy')
    t0 = time.time()
    # To log stat() calls: os.stat = stat_proxy
    sys.setrecursionlimit(2 ** 14)
    if args is None:
        args = sys.argv[1:]

    fscache = FileSystemCache()
    args = [filepath]

    sources, options = process_options(args, stdout=stdout, stderr=stderr,
                                       fscache=fscache)
    messages = []
    formatter = util.FancyFormatter(stdout, stderr, options.show_error_codes)

    def flush_errors(new_messages: List[str], serious: bool) -> None:
        if options.pretty:
            new_messages = formatter.fit_in_terminal(new_messages)
        messages.extend(new_messages)
        f = stderr if serious else stdout
        for msg in new_messages:
            if options.color_output:
                msg = formatter.colorize(msg)
            f.write(msg + '\n')
        f.flush()

    serious = False
    blockers = False
    res = None
    try:
        # Keep a dummy reference (res) for memory profiling below, as otherwise
        # the result could be freed.
        res = build.build(sources, options, None, flush_errors, fscache, stdout, stderr)
    except CompileError as e:
        blockers = True
        if not e.use_stdout:
            serious = True
    if options.warn_unused_configs and options.unused_configs and not options.incremental:
        print("Warning: unused section(s) in %s: %s" %
              (options.config_file,
               ", ".join("[mypy-%s]" % glob for glob in options.per_module_options.keys()
                         if glob in options.unused_configs)),
              file=stderr)
    maybe_write_junit_xml(time.time() - t0, serious, messages, options)

    type_dict = res.types
    list([res])
    return type_dict


if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) < 2:
        print("USAGE: python mypy_infer.py PATH_TO_FILE")
    else:
        filepath = sys.argv[1]
        type_dict = get_type_dict(None, sys.stdout, sys.stderr, filepath=filepath)
        for key, content in type_dict.items():
            if content.__str__() != "Any":

                print("Code: " + key.__str__())
                print("Line Number: " + key.get_line().__str__())
                print("Type: " + content.__str__())
                print()