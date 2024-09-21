# Challenge: Print Hello World in the world's hardest programming language

Welcome to this challenge! You'll be faced with a series of challenging programming languages, trying to print "Hello, World!" in each one.

## Assembly

```assembly
section .text
    global _start

_start:
    ; Write "Hello, World!" to stdout
    mov eax, 4              ; syscall number for sys_write
    mov ebx, 1              ; file descriptor 1 (stdout)
    mov ecx, message        ; pointer to the message
    mov edx, message_len    ; message length
    int 0x80                ; call kernel

    ; Exit the program
    mov eax, 1              ; syscall number for sys_exit
    xor ebx, ebx            ; exit code 0
    int 0x80                ; call kernel

section .data
    message db 'Hello, World!', 10
    message_len equ $ - message
```

## DNS

```dns
01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001
```

## Haskell

```haskell
main = putStrLn "Hello, World!"
```

## Prolog

```prolog
write('Hello, World!').
```

## Erlang

```erlang
-module(hello).
-export([hello_world/0]).

hello_world() -> io:fwrite("Hello, World!\n").
```

## Lisp

```lisp
(format t "Hello, World!")
```

## ADA

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
   Put_Line ("Hello, World!");
end Hello;
```

## Malbolge

```malbolge
(=<`#9]~6ZY32Vx/4Rs+0No-&Jk)"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:'8dc
```

## Brainfuck

```brainfuck
-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.-----------.---.+++.------.--------.-.+.+++++++.
```

## INTERCAL

```intercal
PLEASE NOTE: "Hello, World!"
```

## COW

```cow
MoO MoO mOo MOO mOo MoO mOo mOo mOo mOo mOo mOo mOo MOo mOo mOo MOO mOo mOo mOo MOo mOo mOo MOO mOo MoO MoO MOo MOO MOo mOo MOO mOo
```

## Whitespace

```whitespace
     
      
   
      
   
   
      
      
    
   
     
   
      
    
   
    
   
   
   
    
   
    
   
   
      
   
   
   
    
    
   
   
   
    
   
   
   
     
   
    
   
   
   
    
   
   
   
    
   
    
   
   
   
    
    
   
   
   
    
   
    
   
   
   
    
   
    
   
   
   
    
   
    
   
   
      
   
   
   
    
   
   
   
    
    
   
   
   
    
   
   
   
    
   
   
   
    
    
   
   
   
    
   
    
   
   
   
    
   
    
   
   
   
    
    
   
   
   
    
   
   
   
    
   
   
   
    
   
    
   
   
      
   
   
   
    
   
   
   
    
    
   
   
   
    
   
   
   
    
   
   
   
    
    
   
   
   
    
   
    
   
   
   
    
   
   
   
    
   
    
   
   
      
   
   
   
    
   
   
   
    
    
   
   
   
    
   
   
   
    
   
   
   
    
   
   
   
    
   
    
   
   
   
    
   
    
   
   
   
    
    
   
   
```

These programming languages ​​are indeed challenging and I hope you enjoy the challenge! If you need more help or have any questions, please feel free to ask us.
