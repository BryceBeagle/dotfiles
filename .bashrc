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

export PS1="\[\033[38;5;251m\]┌─[\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;208m\]\u\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;251m\]][\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;39m\]\w\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;251m\]]\n└──\[$(tput sgr0)\]\[\033[38;5;208m\]▪ \[$(tput sgr0)\]"

# Powerline
if [ -f /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh
fi

export EDITOR='nvim'

# export PATH=/tmp/pkgbuild-0/bcompare/src/install/bin:$PATH
export PATH=$PATH:$HOME/.gem/ruby/2.4.0/bin
