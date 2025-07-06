@echo off
setlocal
echo Downloading dependencies...
go mod download

:: Build the project
echo Building the project...
set GOOS=windows
set GOARCH=amd64
go build -o undchain.exe

echo Done. Binary name is: undchain.exe
