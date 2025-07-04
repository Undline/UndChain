#!/bin/bash
set -e

echo "Downloading dependencies..."
go mod download

# Build the project
echo "Building the project..."
GOOS=linux GOARCH=amd64 go build -o undchain

echo "Done. Binary name is : undchain"
