
// Home Page and New Window
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);
user_pref("browser.startup.page", 0);
user_pref("browser.startup.homepage", "about:blank");
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false);
user_pref("browser.tabs.inTitlebar", 0);

// Disable sponsored content on Firefox Home & Clear default topsites
user_pref("browser.newtabpage.activity-stream.showSponsored", false);
user_pref("browser.newtabpage.activity-stream.showSponsoredTopSites", false);
user_pref("browser.newtabpage.activity-stream.default.sites", "");

// Integrated calculator at urlbar
user_pref("browser.urlbar.suggest.calculator", true);
user_pref("font.name.serif.x-western", "Noto Serif");
user_pref("font.name.sans-serif.x-western", "Noto Sans");
user_pref("font.name.monospace.x-western", "JetBrainsMono Nerd Font");
user_pref("browser.display.use_document_fonts", 1);
