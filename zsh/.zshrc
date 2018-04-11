# If not running interactively, don't do anything
[[ -o interactive ]] || return

# Turn on antigen
source /usr/share/zsh/share/antigen.zsh 

# Load the oh-my-zsh core library
antigen use oh-my-zsh

# Install plugins
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle robbyrussell/oh-my-zsh plugins/extract

antigen theme ~/.dotfiles/zsh/theme twoline --no-local-clone

# We're finished making changes
antigen apply

# Set up terminal colors
autoload -U colors && colors
setopt promptsubst



if [ "$TERM" = "linux" ]; then
    echo -en "\e]PB657b83" # S_base00
    echo -en "\e]PA586e75" # S_base01
    echo -en "\e]P0073642" # S_base02
    echo -en "\e]P62aa198" # S_cyan
    echo -en "\e]P8002b36" # S_base03
    echo -en "\e]P2859900" # S_green
    echo -en "\e]P5d33682" # S_magenta
    echo -en "\e]P1dc322f" # S_red
    echo -en "\e]PC839496" # S_base0
    echo -en "\e]PE93a1a1" # S_base1
    echo -en "\e]P9cb4b16" # S_orange
    echo -en "\e]P7eee8d5" # S_base2
    echo -en "\e]P4268bd2" # S_blue
    echo -en "\e]P3b58900" # S_yellow
    echo -en "\e]PFfdf6e3" # S_base3
    echo -en "\e]PD6c71c4" # S_violet
    clear # against bg artifacts
fi

# Aliases
alias ls="ls --color=auto"
alias ll="ls -lh"
alias la="ls -ah"

alias gk="git push"
alias gp="git pull"
alias gc="git commit"
alias ga="git add"
alias gs="git status"

alias dd="dd status=progress"

chpwd() {
    ls --color=auto
}

# Default editor
export EDITOR='nvim'

# virtualenv
export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/bin/virtualenvwrapper.sh

# Path additions
export PATH=$PATH:/usr/local/avr32/bin
