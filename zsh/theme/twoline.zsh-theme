fg[grey]="%F{252}"
fg[orange]="%F{208}"
fg[blue]="%F{39}"
fg[default]="%F{208}"

local fl_open="$fg[grey]┌─"
local username="$fg[grey][$fg[orange]%n$fg[grey]]"
local pwd="$fg[grey][$fg[blue]${PWD/$HOME/~}$fg[grey]]"
local sl_open="$fg[grey]└──"
local dot="$fg[orange]▪"
local sl_close="%{$reset_color%} "

local first_line="${fl_open}${username}${pwd}"
local second_line="${sl_open}${dot}${sl_close}"

PROMPT="${first_line}
${second_line}"

