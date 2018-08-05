# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Terminal Tweaks
[[ $- = *i* ]] && bind TAB:menu-complete   # Windows style tab completion
stty -ixon                                 # Enable use of Ctrl-S

# Aliases
alias ls="ls --color=auto"
alias ll="ls -lh"
alias la="ls -ah"

alias gp="git push"
alias gu="git pull"                        # gu = git update
alias gc="git commit"
alias ga="git add"
alias gs="git status"

alias dd="dd status=progress"

function cd {                              # ls after every cd
    builtin cd "$@" && ls
}

function mkcd {
    mkdir -p "$@" && cd "$@"
}	

# Color Scheme
export PS1="\[\033[38;5;251m\]┌─[\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;208m\]\u\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;251m\]][\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;39m\]\w\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;251m\]]\n└──\[$(tput sgr0)\]\[\033[38;5;208m\]▪ \[$(tput sgr0)\]"

# Default editor
export EDITOR='nvim'

# Path additions
export PATH=$PATH:/usr/local/avr32/bin
