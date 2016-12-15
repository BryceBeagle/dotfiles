#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ $- = *i* ]] && bind TAB:menu-complete

alias ls="ls --color=auto"
alias spac="sudo pacman -S"
alias spaca="sudo apacman -S"
alias spacu="sudo pacman -U"
alias sshgen="ssh bbeagle@general.asu.edu"
alias enw="emacs -nw"
alias x=extract
alias bashrc="enw ~/.bashrc"
alias update="sudo apacman -Syu"
alias kdown="python2 ~/Documents/Scripts/kisscartoon.py"
alias replex="python ~/Documents/Scripts/FileRenamer2.py"
alias spip="sudo pip install"
alias hotbox="sudo mount -t ntfs-3g /dev/sdb1 /mnt/HotBox"

# Extract file using 'x'
extract() {
    tar xzf *.tar.gz
    cd *
    makepkg -s
    spacu *.tar.xz
}

PS1='[\u@\h \W]\$ '

# export PS1="\[\033[38;5;82m\]\u\[$(tput sgr0)\]\[\033[38;5;7m\]@\[$(tput sgr0)\]\[\033[38;5;214m\]\w\[$(tput sgr0)\]\[\033[38;5;7m\]:\[$(tput sgr0)\]"

# export PS1="┌─[\h][\[$(tput sgr0)\]\[\033[38;5;33m\]\w\[$(tput sgr0)\]\[\033[38;5;15m\]]\n└──\[$(tput sgr0)\]\[\033[38;5;4m\]▪ \[$(tput sgr0)\]"

export PS1="┌─[\h][\[$(tput sgr0)\]\[\033[38;5;82m\]\w\[$(tput sgr0)\]\[\033[38;5;7m\]]\n└──\[$(tput sgr0)\]\[\033[38;5;82m\]▪ \[$(tput sgr0)\]"

# Powerline
if [ -f /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh
fi

export EDITOR='emacs -nw'

export PATH=/tmp/pkgbuild-0/bcompare/src/install/bin:$PATH
