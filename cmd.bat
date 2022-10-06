@echo off
set  N=%1
set  M=%2
set T=%N%
set K=1
set /a C=%M%/%N%
set /A F=%M%%%%N%
:1
     for /L %%i in (1, 1, 5000) do (
  TIMEOUT /T %N%
  mkdir %%i
  cd %%i
  echo %T% >> %K%.txt
  set /A K=%K%+1
  set /A T=%T%+%N%
  echo "a new file has been created"
IF %K%==%C% (
 timeout /T %F%
          exit )
goto 1
    )
    pause








