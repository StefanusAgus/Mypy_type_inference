
# Mypy Type Inference

## Requirements
AndroEvolve is compiled with several dependencies:

 - astunparse==1.6.3
 - mypy==0.812
 - The library/types to be inferred must be a built-in type (e.g., int, str, etc.) or from libraries that provide PEP 484 type annotation. 
For example, see:
     - https://github.com/pytorch/pytorch/issues/16574 for PyTorch
     - https://numpy.org/devdocs/reference/typing.html for Numpy

## File Description

1. **mypy.ini** 
Contains the running configuration for mypy. Has been set to export the types inferred. For more details, please refer to:
https://mypy.readthedocs.io/en/stable/config_file.html
2. **mypy_infer.py**
The minimal running example to run the type inference using Mypy. To run the code, simply use the following:
    ```
    python mypy_infer.py PATH_TO_FILE
    ```
    The path to file argument should be changed to the path of the file that which type will be inferred.
3. **1.py**
An example file to run the mypy_infer.py


## Example
After running the mypy_infer.py to the 1.py file, the following output is expected:
```
1.py:26: error: Incompatible types in assignment (expression has type "Tensor", variable has type "List[List[float]]")
1.py:29: error: Module has no attribute "gels"
1.py:29: error: Argument 1 to "cat" has incompatible type "Tuple[Tensor, List[List[float]]]"; expected "Union[Tuple[Tensor, ...], List[Tensor]]"
1.py:32: error: "List[List[float]]" has no attribute "mean"
1.py:33: error: "List[List[float]]" has no attribute "std"
Code: StrExpr(\u000aUses the nn library along with auto-differentiation to define and train, using\u000abatch gradient descent, a neural net that finds the ordinary least-squares\u000aregression plane. The data are mean centered and normalized.  The plane obtained\u000avia gradient descent is compared with the one obtained by solving the normal\u000aequations.\u000a)
Line Number: 3
Type: Literal['\nUses the nn library along with auto-differentiation to define and train, using\nbatch gradient descent, a neural net that finds the ordinary least-squares\nregression plane. The data are mean centered and normalized.  The plane obtained\nvia gradient descent is compared with the one obtained by solving the normal\nequations.\n']?

Code: NameExpr(open [builtins.open])
Line Number: 16
Type: Overload(def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['r'], Literal['r+'], Literal['+r'], Literal['rt'], Literal['tr'], Literal['rt+'], Literal['r+t'], Literal['+rt'], Literal['tr+'], Literal['t+r'], Literal['+tr'], Literal['w'], Literal['w+'], Literal['+w'], Literal['wt'], Literal['tw'], Literal['wt+'], Literal['w+t'], Literal['+wt'], Literal['tw+'], Literal['t+w'], Literal['+tw'], Literal['a'], Literal['a+'], Literal['+a'], Literal['at'], Literal['ta'], Literal['at+'], Literal['a+t'], Literal['+at'], Literal['ta+'], Literal['t+a'], Literal['+ta'], Literal['x'], Literal['x+'], Literal['+x'], Literal['xt'], Literal['tx'], Literal['xt+'], Literal['x+t'], Literal['+xt'], Literal['tx+'], Literal['t+x'], Literal['+tx'], Literal['U'], Literal['rU'], Literal['Ur'], Literal['rtU'], Literal['rUt'], Literal['Urt'], Literal['trU'], Literal['tUr'], Literal['Utr']] =, buffering: builtins.int =, encoding: Union[builtins.str, None] =, errors: Union[builtins.str, None] =, newline: Union[builtins.str, None] =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> io.TextIOWrapper, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['rb+'], Literal['r+b'], Literal['+rb'], Literal['br+'], Literal['b+r'], Literal['+br'], Literal['wb+'], Literal['w+b'], Literal['+wb'], Literal['bw+'], Literal['b+w'], Literal['+bw'], Literal['ab+'], Literal['a+b'], Literal['+ab'], Literal['ba+'], Literal['b+a'], Literal['+ba'], Literal['xb+'], Literal['x+b'], Literal['+xb'], Literal['bx+'], Literal['b+x'], Literal['+bx'], Literal['rb'], Literal['br'], Literal['rbU'], Literal['rUb'], Literal['Urb'], Literal['brU'], Literal['bUr'], Literal['Ubr'], Literal['wb'], Literal['bw'], Literal['ab'], Literal['ba'], Literal['xb'], Literal['bx']], buffering: Literal[0], encoding: None =, errors: None =, newline: None =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> io.FileIO, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['rb+'], Literal['r+b'], Literal['+rb'], Literal['br+'], Literal['b+r'], Literal['+br'], Literal['wb+'], Literal['w+b'], Literal['+wb'], Literal['bw+'], Literal['b+w'], Literal['+bw'], Literal['ab+'], Literal['a+b'], Literal['+ab'], Literal['ba+'], Literal['b+a'], Literal['+ba'], Literal['xb+'], Literal['x+b'], Literal['+xb'], Literal['bx+'], Literal['b+x'], Literal['+bx']], buffering: Union[Literal[-1], Literal[1]] =, encoding: None =, errors: None =, newline: None =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> io.BufferedRandom, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['wb'], Literal['bw'], Literal['ab'], Literal['ba'], Literal['xb'], Literal['bx']], buffering: Union[Literal[-1], Literal[1]] =, encoding: None =, errors: None =, newline: None =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> io.BufferedWriter, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['rb'], Literal['br'], Literal['rbU'], Literal['rUb'], Literal['Urb'], Literal['brU'], Literal['bUr'], Literal['Ubr']], buffering: Union[Literal[-1], Literal[1]] =, encoding: None =, errors: None =, newline: None =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> io.BufferedReader, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: Union[Literal['rb+'], Literal['r+b'], Literal['+rb'], Literal['br+'], Literal['b+r'], Literal['+br'], Literal['wb+'], Literal['w+b'], Literal['+wb'], Literal['bw+'], Literal['b+w'], Literal['+bw'], Literal['ab+'], Literal['a+b'], Literal['+ab'], Literal['ba+'], Literal['b+a'], Literal['+ba'], Literal['xb+'], Literal['x+b'], Literal['+xb'], Literal['bx+'], Literal['b+x'], Literal['+bx'], Literal['rb'], Literal['br'], Literal['rbU'], Literal['rUb'], Literal['Urb'], Literal['brU'], Literal['bUr'], Literal['Ubr'], Literal['wb'], Literal['bw'], Literal['ab'], Literal['ba'], Literal['xb'], Literal['bx']], buffering: builtins.int, encoding: None =, errors: None =, newline: None =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> typing.BinaryIO, def (file: Union[builtins.str, builtins.bytes, builtins._PathLike[builtins.str], builtins._PathLike[builtins.bytes], builtins.int], mode: builtins.str, buffering: builtins.int =, encoding: Union[builtins.str, None] =, errors: Union[builtins.str, None] =, newline: Union[builtins.str, None] =, closefd: builtins.bool =, opener: Union[def (builtins.str, builtins.int) -> builtins.int, None] =) -> typing.IO[Any])

Code: StrExpr(temp_co2_data.csv)
Line Number: 16
Type: Literal['temp_co2_data.csv']?

Code: CallExpr:16(
  NameExpr(open [builtins.open])
  Args(
    StrExpr(temp_co2_data.csv)))
Line Number: 16
Type: typing.TextIO

Code: TempNode:16(
  typing.TextIO)
Line Number: 16
Type: typing.TextIO

Code: NameExpr(csvfile* [1.csvfile])
Line Number: 16
Type: typing.TextIO

Code: MemberExpr:17(
  NameExpr(csv)
  reader [_csv.reader])
Line Number: 17
Type: def (csvfile: typing.Iterable[builtins.str], dialect: Union[builtins.str, _csv.Dialect, Type[_csv.Dialect]] =, **fmtparams: Any) -> _csv._reader

Code: NameExpr(csvfile [1.csvfile])
Line Number: 17
Type: typing.TextIO

Code: StrExpr(,)
Line Number: 17
Type: Literal[',']?

Code: CallExpr:17(
  MemberExpr:17(
    NameExpr(csv)
    reader [_csv.reader])
  Args(
    NameExpr(csvfile [1.csvfile]))
  KwArgs(
    delimiter
    StrExpr(,)))
Line Number: 17
Type: _csv._reader

Code: NameExpr(reader* [1.reader])
Line Number: 17
Type: _csv._reader

Code: NameExpr(next [builtins.next])
Line Number: 18
Type: Overload(def [_T] (typing.Iterator[_T`-1]) -> _T`-1, def [_T, _VT] (typing.Iterator[_T`-1], default: _VT`-2) -> Union[_T`-1, _VT`-2])

Code: NameExpr(csvfile [1.csvfile])
Line Number: 18
Type: typing.TextIO

Code: CallExpr:18(
  NameExpr(next [builtins.next])
  Args(
    NameExpr(csvfile [1.csvfile])))
Line Number: 18
Type: builtins.str*

Code: ListExpr:19()
Line Number: 19
Type: builtins.list[<nothing>]

Code: NameExpr(xss* [1.xss])
Line Number: 19
Type: <partial list[?]>

Code: ListExpr:19()
Line Number: 19
Type: builtins.list[<nothing>]

Code: NameExpr(yss* [1.yss])
Line Number: 19
Type: <partial list[?]>

Code: NameExpr(reader [1.reader])
Line Number: 20
Type: _csv._reader

Code: TempNode:20(
  builtins.list*[builtins.str])
Line Number: 20
Type: builtins.list*[builtins.str]

Code: NameExpr(row* [1.row])
Line Number: 20
Type: builtins.list*[builtins.str]

Code: NameExpr(float [builtins.float])
Line Number: 21
Type: def (x: Union[typing.SupportsFloat, builtins._SupportsIndex, builtins.str] =) -> builtins.float*

Code: NameExpr(row [1.row])
Line Number: 21
Type: builtins.list*[builtins.str]

Code: IntExpr(2)
Line Number: 21
Type: Literal[2]?

Code: IndexExpr:21(
  NameExpr(row [1.row])
  IntExpr(2))
Line Number: 21
Type: builtins.str*

Code: CallExpr:21(
  NameExpr(float [builtins.float])
  Args(
    IndexExpr:21(
      NameExpr(row [1.row])
      IntExpr(2))))
Line Number: 21
Type: builtins.float*

Code: NameExpr(float [builtins.float])
Line Number: 21
Type: def (x: Union[typing.SupportsFloat, builtins._SupportsIndex, builtins.str] =) -> builtins.float*

Code: NameExpr(row [1.row])
Line Number: 21
Type: builtins.list*[builtins.str]

Code: IntExpr(3)
Line Number: 21
Type: Literal[3]?

Code: IndexExpr:21(
  NameExpr(row [1.row])
  IntExpr(3))
Line Number: 21
Type: builtins.str*

Code: CallExpr:21(
  NameExpr(float [builtins.float])
  Args(
    IndexExpr:21(
      NameExpr(row [1.row])
      IntExpr(3))))
Line Number: 21
Type: builtins.float*

Code: ListExpr:21(
  CallExpr:21(
    NameExpr(float [builtins.float])
    Args(
      IndexExpr:21(
        NameExpr(row [1.row])
        IntExpr(2))))
  CallExpr:21(
    NameExpr(float [builtins.float])
    Args(
      IndexExpr:21(
        NameExpr(row [1.row])
        IntExpr(3)))))
Line Number: 21
Type: builtins.list[builtins.float]

Code: NameExpr(xss [1.xss])
Line Number: 21
Type: builtins.list[builtins.list[builtins.float*]]

Code: MemberExpr:21(
  NameExpr(xss [1.xss])
  append)
Line Number: 21
Type: def (builtins.list*[builtins.float*])

Code: CallExpr:21(
  MemberExpr:21(
    NameExpr(xss [1.xss])
    append)
  Args(
    ListExpr:21(
      CallExpr:21(
        NameExpr(float [builtins.float])
        Args(
          IndexExpr:21(
            NameExpr(row [1.row])
            IntExpr(2))))
      CallExpr:21(
        NameExpr(float [builtins.float])
        Args(
          IndexExpr:21(
            NameExpr(row [1.row])
            IntExpr(3)))))))
Line Number: 21
Type: None

Code: NameExpr(float [builtins.float])
Line Number: 22
Type: def (x: Union[typing.SupportsFloat, builtins._SupportsIndex, builtins.str] =) -> builtins.float*

Code: NameExpr(row [1.row])
Line Number: 22
Type: builtins.list*[builtins.str]

Code: IntExpr(1)
Line Number: 22
Type: Literal[1]?

Code: IndexExpr:22(
  NameExpr(row [1.row])
  IntExpr(1))
Line Number: 22
Type: builtins.str*

Code: CallExpr:22(
  NameExpr(float [builtins.float])
  Args(
    IndexExpr:22(
      NameExpr(row [1.row])
      IntExpr(1))))
Line Number: 22
Type: builtins.float*

Code: ListExpr:22(
  CallExpr:22(
    NameExpr(float [builtins.float])
    Args(
      IndexExpr:22(
        NameExpr(row [1.row])
        IntExpr(1)))))
Line Number: 22
Type: builtins.list[builtins.float]

Code: NameExpr(yss [1.yss])
Line Number: 22
Type: builtins.list[builtins.list[builtins.float*]]

Code: MemberExpr:22(
  NameExpr(yss [1.yss])
  append)
Line Number: 22
Type: def (builtins.list*[builtins.float*])

Code: CallExpr:22(
  MemberExpr:22(
    NameExpr(yss [1.yss])
    append)
  Args(
    ListExpr:22(
      CallExpr:22(
        NameExpr(float [builtins.float])
        Args(
          IndexExpr:22(
            NameExpr(row [1.row])
            IntExpr(1)))))))
Line Number: 22
Type: None

Code: NameExpr(xss [1.xss])
Line Number: 26
Type: builtins.list[builtins.list[builtins.float*]]

Code: MemberExpr:26(
  NameExpr(torch)
  tensor [torch._C._VariableFunctions.tensor])
Line Number: 26
Type: def (data: Any, dtype: Union[torch._C.dtype, None] =, device: Union[torch._C.device, builtins.str, None] =, requires_grad: builtins.bool =) -> torch.tensor.Tensor

Code: NameExpr(xss [1.xss])
Line Number: 26
Type: builtins.list[builtins.list[builtins.float*]]

Code: CallExpr:26(
  MemberExpr:26(
    NameExpr(torch)
    tensor [torch._C._VariableFunctions.tensor])
  Args(
    NameExpr(xss [1.xss])))
Line Number: 26
Type: torch.tensor.Tensor

Code: NameExpr(yss [1.yss])
Line Number: 26
Type: builtins.list[builtins.list[builtins.float*]]

Code: MemberExpr:26(
  NameExpr(torch)
  tensor [torch._C._VariableFunctions.tensor])
Line Number: 26
Type: def (data: Any, dtype: Union[torch._C.dtype, None] =, device: Union[torch._C.device, builtins.str, None] =, requires_grad: builtins.bool =) -> torch.tensor.Tensor

Code: NameExpr(yss [1.yss])
Line Number: 26
Type: builtins.list[builtins.list[builtins.float*]]

Code: CallExpr:26(
  MemberExpr:26(
    NameExpr(torch)
    tensor [torch._C._VariableFunctions.tensor])
  Args(
    NameExpr(yss [1.yss])))
Line Number: 26
Type: torch.tensor.Tensor

Code: NameExpr(torch)
Line Number: 29
Type: _importlib_modulespec.ModuleType

Code: NameExpr(yss [1.yss])
Line Number: 29
Type: builtins.list[builtins.list[builtins.float*]]

Code: MemberExpr:29(
  NameExpr(torch)
  cat [torch._C._VariableFunctions.cat])
Line Number: 29
Type: Overload(def (tensors: Union[builtins.tuple[torch.tensor.Tensor], builtins.list[torch.tensor.Tensor]], dim: Union[builtins.str, builtins.ellipsis, None], *, out: Union[torch.tensor.Tensor, None] =) -> torch.tensor.Tensor, def (tensors: Union[builtins.tuple[torch.tensor.Tensor], builtins.list[torch.tensor.Tensor]], dim: builtins.int =, *, out: Union[torch.tensor.Tensor, None] =) -> torch.tensor.Tensor)

Code: MemberExpr:29(
  NameExpr(torch)
  ones [torch._C._VariableFunctions.ones])
Line Number: 29
Type: Overload(def (size: Union[torch._C.Size, builtins.list[builtins.int], builtins.tuple[builtins.int]], *, names: Union[typing.Sequence[Union[builtins.str, builtins.ellipsis, None]], None], dtype: Union[torch._C.dtype, None] =, layout: Union[torch._C.layout, None] =, device: Union[torch._C.device, builtins.str, None] =, pin_memory: builtins.bool =, requires_grad: builtins.bool =) -> torch.tensor.Tensor, def (*size: builtins.int, *, names: Union[typing.Sequence[Union[builtins.str, builtins.ellipsis, None]], None], dtype: Union[torch._C.dtype, None] =, layout: Union[torch._C.layout, None] =, device: Union[torch._C.device, builtins.str, None] =, pin_memory: builtins.bool =, requires_grad: builtins.bool =) -> torch.tensor.Tensor, def (size: Union[torch._C.Size, builtins.list[builtins.int], builtins.tuple[builtins.int]], *, out: Union[torch.tensor.Tensor, None] =, dtype: Union[torch._C.dtype, None] =, layout: Union[torch._C.layout, None] =, device: Union[torch._C.device, builtins.str, None] =, pin_memory: builtins.bool =, requires_grad: builtins.bool =) -> torch.tensor.Tensor, def (*size: builtins.int, *, out: Union[torch.tensor.Tensor, None] =, dtype: Union[torch._C.dtype, None] =, layout: Union[torch._C.layout, None] =, device: Union[torch._C.device, builtins.str, None] =, pin_memory: builtins.bool =, requires_grad: builtins.bool =) -> torch.tensor.Tensor)

Code: NameExpr(len [builtins.len])
Line Number: 29
Type: def (typing.Sized) -> builtins.int

Code: NameExpr(xss [1.xss])
Line Number: 29
Type: builtins.list[builtins.list[builtins.float*]]

Code: CallExpr:29(
  NameExpr(len [builtins.len])
  Args(
    NameExpr(xss [1.xss])))
Line Number: 29
Type: builtins.int

Code: IntExpr(1)
Line Number: 29
Type: Literal[1]?

Code: CallExpr:29(
  MemberExpr:29(
    NameExpr(torch)
    ones [torch._C._VariableFunctions.ones])
  Args(
    CallExpr:29(
      NameExpr(len [builtins.len])
      Args(
        NameExpr(xss [1.xss])))
    IntExpr(1)))
Line Number: 29
Type: torch.tensor.Tensor

Code: NameExpr(xss [1.xss])
Line Number: 29
Type: builtins.list[builtins.list[builtins.float*]]

Code: TupleExpr:29(
  CallExpr:29(
    MemberExpr:29(
      NameExpr(torch)
      ones [torch._C._VariableFunctions.ones])
    Args(
      CallExpr:29(
        NameExpr(len [builtins.len])
        Args(
          NameExpr(xss [1.xss])))
      IntExpr(1)))
  NameExpr(xss [1.xss]))
Line Number: 29
Type: Tuple[torch.tensor.Tensor, builtins.list[builtins.list[builtins.float*]]]

Code: IntExpr(1)
Line Number: 29
Type: Literal[1]?

Code: CallExpr:29(
  MemberExpr:29(
    NameExpr(torch)
    cat [torch._C._VariableFunctions.cat])
  Args(
    TupleExpr:29(
      CallExpr:29(
        MemberExpr:29(
          NameExpr(torch)
          ones [torch._C._VariableFunctions.ones])
        Args(
          CallExpr:29(
            NameExpr(len [builtins.len])
            Args(
              NameExpr(xss [1.xss])))
          IntExpr(1)))
      NameExpr(xss [1.xss]))
    IntExpr(1)))
Line Number: 29
Type: torch.tensor.Tensor

Code: NameExpr(xss [1.xss])
Line Number: 32
Type: builtins.list[builtins.list[builtins.float*]]

Code: IntExpr(0)
Line Number: 32
Type: Literal[0]?

Code: NameExpr(yss [1.yss])
Line Number: 32
Type: builtins.list[builtins.list[builtins.float*]]

Code: NameExpr(xss [1.xss])
Line Number: 33
Type: builtins.list[builtins.list[builtins.float*]]

Code: IntExpr(0)
Line Number: 33
Type: Literal[0]?

Code: NameExpr(yss [1.yss])
Line Number: 33
Type: builtins.list[builtins.list[builtins.float*]]
```

