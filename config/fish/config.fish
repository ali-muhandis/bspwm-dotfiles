
# Create aliases
alias cls="clear"
alias g="git"
alias n="nvim"
alias m="micro"
alias cat="bat"
alias ls="eza --icons"
alias ll="eza -la --icons --git"
alias lt="eza --tree --icons --level=2"
alias feh="feh --scale-down"

alias reflector_update="sudo reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorlist"

# Display critical errors
alias syslog_emerg="sudo dmesg --level=emerg,alert,crit"

# Output common errors
alias syslog="sudo dmesg --level=err,warn"

# Print logs from x server
alias xlog='grep "(EE)\|(WW)\|error\|failed" ~/.local/share/xorg/Xorg.0.log'

# Remove archived journal files until the disk space they use falls below 100M
alias vacuum="journalctl --vacuum-size=100M"

# Make all journal files contain no data older than 2 weeks
alias vacuum_time="journalctl --vacuum-time=2weeks"

set -U fish_greeting
set fish_color_command green
set -gx EDITOR micro
set -gx VISUAL micro
set -gx BROWSER /usr/bin/firefox


if status is-interactive
    # SSH agent
    if test -z "$SSH_AUTH_SOCK"
        eval (ssh-agent -c) > /dev/null
        ssh-add ~/.ssh/id_ed25519 2>/dev/null
        ssh-add ~/.ssh/edukit_ed25519 2>/dev/null
        ssh-add ~/.ssh/owa_payroll_ed25519 2>/dev/null
    end

    # Show homepage in tmux
    if set -q TMUX
        ~/bin/tmux-home
    end
end

starship init fish | source
zoxide init fish | source
fzf --fish | source

set -gx PATH $PATH /opt/android-sdk/cmdline-tools/latest/bin
set -gx PATH $PATH /opt/android-sdk/platform-tools
set -gx ANDROID_HOME /opt/android-sdk
set -gx CHROME_EXECUTABLE /usr/bin/chromium
set -gx XCURSOR_THEME catppuccin-mocha-blue-cursors
set -gx XCURSOR_SIZE 24
export PATH="$HOME/.local/bin:$PATH"
