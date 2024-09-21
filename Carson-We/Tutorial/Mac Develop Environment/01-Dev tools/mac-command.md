# Useful Mac Commands

## Time Machine

- Time Machine accelerate
`
sudo sysctl debug.lowpri_throttle_enabled=0
`
- Revert
`
sudo sysctl debug.lowpri_throttle_enabled=1
`

## File System

- List files and directories in the current directory:
  `
  ls
  `
- Change directory:
  `
  cd [directory_path]
  `
- Create a new directory:
  `
  mkdir [directory_name]
  `

## System Information

- Show system information:
  `
  system_profiler
  `
- Display system uptime:
  `
  uptime
  `

## Network

- Display network configuration:
  `
  ifconfig
  `
- Check network connections:
  `
  netstat
  `

## Processes

- List running processes:
  `
  ps
  `
- Kill a process:
  `
  kill [process_id]
  `

## Package Management

- Install Homebrew (package manager for macOS):
  `
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  `
- Install a package using Homebrew:
  `
  brew install [package_name]
  `

## Disk Space

- Display disk space usage:
  `
  df -h
  `

## Terminal

- Clear the terminal screen:
  `
  clear
  `
- Search command history:
  `
  history | grep [keyword]
  `

## User Management

- Add a new user:
  `
  sudo sysadminctl -addUser [username]
  `
- Change user password:
  `
  passwd [username]
  `

## Miscellaneous

- Open a file or directory in Finder:
  `
  open [file_path]
  `
- Shutdown macOS after a specified delay:
  `
  shutdown -h +60 "Shutting down in 1 hour"
  `
  