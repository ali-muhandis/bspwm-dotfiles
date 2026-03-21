import os
import packages

from logger import Logger, LoggerStatus
from creators.software import AurBuilder, FirefoxCustomize
from creators.patches import PatchSystemBugs
from creators.daemons import Daemons


class SystemConfiguration:
    def start(*args):
        start_text = f"[+] Starting assembly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)
        if args[0]: SystemConfiguration.__start_option_1()
        if args[1]: SystemConfiguration.__start_option_2()
        if args[2]: SystemConfiguration.__start_option_3()
        if args[3]: SystemConfiguration.__start_option_4()

        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()
        SystemConfiguration.__post_install()

    @staticmethod
    def __start_option_1():
        SystemConfiguration.__create_default_folders()
        SystemConfiguration.__copy_bspwm_dotfiles()

    @staticmethod
    def __start_option_2():
        Logger.add_record("[+] Updates Enabled", status=LoggerStatus.SUCCESS)
        os.system("sudo pacman -Syu")

    @staticmethod
    def __start_option_3():
        Logger.add_record("[+] Installed BSPWM Dependencies", status=LoggerStatus.SUCCESS)
        AurBuilder.build()
        SystemConfiguration.__install_pacman_package(packages.BASE_PACKAGES)
        SystemConfiguration.__install_aur_package(packages.AUR_PACKAGES)
        FirefoxCustomize.build()

    @staticmethod
    def __start_option_4():
        Logger.add_record("[+] Installed Dev Dependencies", status=LoggerStatus.SUCCESS)
        SystemConfiguration.__install_pacman_package(packages.DEV_PACKAGES)

    @staticmethod
    def __install_pacman_package(package_names: list):
        for package in package_names:
            os.system(f"sudo pacman -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    def __install_aur_package(package_names: list):
        for package in package_names:
            os.system(f"yay -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    def __create_default_folders():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        default_folders = "~/Videos ~/Documents ~/Downloads ~/Music ~/Desktop ~/pictures/wallpapers ~/work"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")
        os.system("cp -r Images/ ~/pictures/wallpapers/")

    @staticmethod
    def __copy_bspwm_dotfiles():
        Logger.add_record("[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS)
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")

        # Tmux config
        os.system("cp .tmux.conf ~/")

        # Cursor theme
        os.system("mkdir -p ~/.icons/default")
        os.system("cp config/icons-default/index.theme ~/.icons/default/")

    @staticmethod
    def __post_install():
        Logger.add_record("[+] Running post-install setup", status=LoggerStatus.SUCCESS)

        # Tmux plugins
        os.system("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
        os.system("git clone https://github.com/tmux-plugins/tmux-resurrect ~/.tmux/plugins/tmux-resurrect")
        os.system("git clone https://github.com/tmux-plugins/tmux-continuum ~/.tmux/plugins/tmux-continuum")
        os.system("git clone https://github.com/tmux-plugins/tmux-yank ~/.tmux/plugins/tmux-yank")
        os.system("git clone https://github.com/tmux-plugins/tmux-open ~/.tmux/plugins/tmux-open")
        os.system("git clone https://github.com/fcsonline/tmux-thumbs ~/.tmux/plugins/tmux-thumbs")
        os.system("git clone https://github.com/sainnhe/tmux-fzf ~/.tmux/plugins/tmux-fzf")
        Logger.add_record("[+] Tmux plugins installed", status=LoggerStatus.SUCCESS)

        # Git config
        os.system('git config --global user.name "Ali Odiljonov"')
        os.system('git config --global user.email "a.odiljonov@openweb.uz"')
        os.system('git config --global init.defaultBranch main')
        Logger.add_record("[+] Git config set", status=LoggerStatus.SUCCESS)

        # PostgreSQL setup
        os.system("sudo -u postgres initdb -D /var/lib/postgres/data 2>/dev/null")
        os.system("sudo systemctl enable --now postgresql")
        os.system("sudo -u postgres createuser -s $(whoami) 2>/dev/null")
        os.system("sudo -u postgres createdb $(whoami) 2>/dev/null")
        Logger.add_record("[+] PostgreSQL configured", status=LoggerStatus.SUCCESS)

        # SDDM theme
        os.system("sudo cp -r /usr/share/sddm/themes/sddm-astronaut /usr/share/sddm/themes/sddm-astronaut-backup 2>/dev/null")
        sddm_conf = '[Theme]\nCurrent=sddm-astronaut\n\n[General]\nInputMethod=\n\n[X11]\nMinimumVT=1'
        os.system(f'echo -e "{sddm_conf}" | sudo tee /etc/sddm.conf.d/theme.conf')
        os.system("sudo systemctl enable sddm")
        Logger.add_record("[+] SDDM configured", status=LoggerStatus.SUCCESS)

        # UFW firewall
        os.system("sudo ufw default deny incoming")
        os.system("sudo ufw default allow outgoing")
        os.system("sudo ufw --force enable")
        os.system("sudo systemctl enable ufw")
        Logger.add_record("[+] UFW firewall enabled", status=LoggerStatus.SUCCESS)

        # Timeshift + cronie
        os.system("sudo systemctl enable --now cronie 2>/dev/null")
        Logger.add_record("[+] Timeshift cronie enabled", status=LoggerStatus.SUCCESS)

        # Disable screen saver
        os.system("xset s off 2>/dev/null")
        os.system("xset -dpms 2>/dev/null")
        os.system("xset s noblank 2>/dev/null")
