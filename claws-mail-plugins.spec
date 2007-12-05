%define oname claws-mail
%define claws_version 3.1.0
%define cvs %nil

Summary:    This package contains additional plugins for %{oname}
Name:       %{oname}-plugins
Version:    %{claws_version}
Release:    %mkrel 3
Group:      Networking/Mail
License:    GPL
URL:        http://www.claws-mail.org/plugins/downloads
Source:     %{oname}-extra-plugins-%{version}%{cvs}.tar.bz2
Buildroot:  %{_tmppath}/%{name}-buildroot
BuildRequires:  claws-mail-devel = 1:%{claws_version}
BuildRequires:  claws-mail = 1:%{claws_version}
BuildRequires:  libsynce-devel
BuildRequires:  libetpan-devel
BuildRequires:  perl-devel
BuildRequires:  curl-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  automake1.9
BuildRequires:  libgtkhtml2-devel
BuildRequires:  librapi-devel
%if %mdkversion > 200800
BuildRequires:  libytnef-devel
%endif
%if %mdkversion >= 200800
BuildRequires:	libpoppler-devel
BuildRequires:  libpoppler-glib-devel
%else
BuildRequires:	libpoppler1-devel
%endif
BuildRequires:  ghostscript
Requires:   %{oname} = %{claws_version}

%description
This package contains additional plugins for %{oname}:
%{oname}-acpi-plugin,
%{oname}-att_remover-plugin,
%{oname}-cachesaver-plugin,
%{oname}-etpan-privacy-plugin,
%{oname}-fetchinfo-plugin,
%{oname}-maildir-plugin,
%{oname}-mailmbox-plugin,
%{oname}-notification-plugin,
%{oname}-perl-plugin,
%{oname}-rssyl-plugin,
%{oname}-smime-plugin,
%{oname}-synce-plugin,
%{oname}-vcalendar-plugin,
%{oname}-pdfviewer-plugin,
%{oname}-spamreport-plugin,
%{oname}-tnefparse-plugin.

%package -n %{oname}-acpi-plugin
Summary:    This plugin enables mail notification via LEDs on some laptops
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-acpi-plugin
Provides: sylpheed-claws-acpi-plugin

%description -n %{oname}-acpi-plugin
This plugin for %{oname} enables mail notification via LEDs
on some laptops.

%package -n %{oname}-att_remover-plugin
Summary:    This plugin for %{oname} enables the removal of attachments
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-att_remover-plugin
Provides: sylpheed-claws-att_remover-plugin


%description -n %{oname}-att_remover-plugin
This plugin for %{oname} enables the removal of attachments.

%package -n %{oname}-cachesaver-plugin
Summary:    This plugin for %{oname} saves the caches every minute
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-cachesaver-plugin
Obsoletes:  sylpheed-claws2-cachesaver-plugin
Provides:   sylpheed-claws-cachesaver-plugin
Obsoletes:  sylpheed-claws-cachesaver-plugin

%description -n %{oname}-cachesaver-plugin
This plugin for %{oname} saves the caches every minute. It helps
in avoiding the loss of metadata on crashes.

%package -n %{oname}-etpan-privacy-plugin
Summary:    This plugin handles verification and decryption of encrypted messages
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-etpan-privacy-plugin
Obsoletes:  sylpheed-claws2-etpan-privacy-plugin
Provides:   sylpheed-claws-etpan-privacy-plugin
Obsoletes:  sylpheed-claws-etpan-privacy-plugin

%description -n %{oname}-etpan-privacy-plugin
This plugin handles signature verification and decryption of encrypted
messages in S/MIME, OpenPGP, and ascii-armored PGP formats.

%package -n %{oname}-fetchinfo-plugin
Summary:    This plugin inserts headers containing some download information
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-fetchinfo-plugin
Obsoletes:  sylpheed-claws2-fetchinfo-plugin
Provides:   sylpheed-claws-fetchinfo-plugin
Obsoletes:  sylpheed-claws-fetchinfo-plugin

%description -n %{oname}-fetchinfo-plugin
This plugin for %{oname} inserts headers containing some download
information: UIDL, Sylpheeds account name, POP server, user ID
and retrieval time.

%package -n %{oname}-maildir-plugin
Summary:    This plugin provides direct access to maildir folders
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-maildir-plugin
Obsoletes:  sylpheed-claws2-maildir-plugin
Provides:   sylpheed-claws-maildir-plugin
Obsoletes:  sylpheed-claws-maildir-plugin

%description -n %{oname}-maildir-plugin
This plugin for %{oname} provides direct access to maildir folders.

%package -n %{oname}-mailmbox-plugin
Summary:    This plugin provides direct access to mbox folders
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-mailmbox-plugin
Obsoletes:  sylpheed-claws2-mailmbox-plugin
Provides:   sylpheed-claws-mailmbox-plugin
Obsoletes:  sylpheed-claws-mailmbox-plugin

%description -n %{oname}-mailmbox-plugin
This plugin for %{oname} provides direct access to mbox folders

%package -n %{oname}-newmail-plugin
Summary:    This plugin can write a summary to a log file
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-newmail-plugin
Provides: sylpheed-claws-newmail-plugin

%description -n %{oname}-newmail-plugin
This plugin for %{oname} can write a summary to a log file upon
receiving new mail. It defaults to ~/Mail/NewLog.

%package -n %{oname}-notification-plugin
Summary:        This plugin notify from new mail
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-notification-plugin
Provides: sylpheed-claws-notification-plugin

%description -n %{oname}-notification-plugin
This plugin for %{oname} notify from new incoming mail.

%package -n %{oname}-perl-plugin
Summary:    Perl interface to %{oname}s' filtering mechanism
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-perl-plugin
Obsoletes:  sylpheed-claws2-perl-plugin
Provides:   sylpheed-claws-perl_plugin-plugin
Obsoletes:  sylpheed-claws-perl_plugin-plugin

%description -n %{oname}-perl-plugin
This plugin is intended to extend the filtering possibilities
of %{oname}. It provides a Perl interface to %{oname}s'
filtering mechanism, allowing the use of full Perl power in
email filters.

%package -n %{oname}-rssyl-plugin
Summary:    This plugin allows you to read your favorite newsfeeds in %{oname}
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-rssyl-plugin
Provides: sylpheed-claws-rssyl-plugin

%description -n %{oname}-rssyl-plugin
This plugin allows you to read your favorite newsfeeds in %{oname}.
RSS 1.0, 2.0 and Atom feeds are currently supported.

%package -n %{oname}-smime-plugin
Summary:        This plugin allow to use smine in mail
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Obsoletes: sylpheed-claws-smime-plugin
Provides: sylpheed-claws-smime-plugin

%description -n %{oname}-smime-plugin
This plugin for %{oname} allow to use smime in mail.

%package -n %{oname}-synce-plugin
Summary:    This plugin assists in syncing the addressbook
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-synce-plugin
Obsoletes:  sylpheed-claws2-synce-plugin
Provides:   sylpheed-claws-synce-plugin
Obsoletes:  sylpheed-claws-synce-plugin

%description -n %{oname}-synce-plugin
This plugin assists in keeping the addressbook of a Windows CE
device (Pocket PC/ iPAQ, Smartphone etc) in sync with %{oname}s'
addressbook, with respect to email addresses.

%package -n %{oname}-vcalendar-plugin
Summary:    This plugin for %{oname} enables vCalendar message handling
Group:      Networking/Mail
Requires:   %{oname} >= %{claws_version}
Provides:   sylpheed-claws2-vcalendar-plugin
Obsoletes:  sylpheed-claws2-vcalendar-plugin
Provides:   sylpheed-claws-vcalendar-plugin
Obsoletes:  sylpheed-claws-vcalendar-plugin


%description -n %{oname}-vcalendar-plugin
This %{oname} plugin handles the vCalendar format (or rather, the
meeting subset of it). It displays such mails in a nice format, lets you
create and send meetings, and creates a virtual folder with the meetings you
have sent or received.

%package -n %{oname}-gtkhtml2_viewer-plugin
Summary:        This plugin for %{oname} enables gtkhtml2 viewer
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Provides:       sylpheed-claws2-gtkhtml2_viewer-plugin
Obsoletes:      sylpheed-claws2-gtkhtml2_viewer-plugin
Provides:       sylpheed-claws-gtkhtml2_viewer-plugin
Obsoletes:      sylpheed-claws-gtkhtml2_viewer-plugin

%description -n %{oname}-gtkhtml2_viewer-plugin
This %{oname} plugin provides gtkhtml2 viewer.


%package -n %{oname}-attachwarner-plugin
Summary:        This plugin for %{oname} enables attachwarner
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Provides:       sylpheed-claws2-gtkhtml2_viewer-plugin
Obsoletes:      sylpheed-claws2-gtkhtml2_viewer-plugin
Provides:       sylpheed-claws-gtkhtml2_viewer-plugin
Obsoletes:      sylpheed-claws-gtkhtml2_viewer-plugin

%description -n %{oname}-attachwarner-plugin
This %{oname} plugin provides attachwarner.

%package -n %{oname}-pdf_viewer-plugin
Summary:        This plugin for %{oname} enables pdf_viewer
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Provides:       sylpheed-claws2-pdf_viewer-plugin
Obsoletes:      sylpheed-claws2-pdf_viewer-plugin
Provides:       sylpheed-claws-pdf_viewer-plugin
Obsoletes:      sylpheed-claws-pdf_viewer-plugin

%description -n %{oname}-pdf_viewer-plugin
This %{oname} plugin provides pdf_viewer.

%package -n %{oname}-spam_report-plugin
Summary:        This plugin for %{oname} enables spamreport
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Provides:       sylpheed-claws2-spam_report-plugin
Obsoletes:      sylpheed-claws2-spam_report-plugin
Provides:       sylpheed-claws-spam_report-plugin
Obsoletes:      sylpheed-claws-spam_report-plugin

%description -n %{oname}-spam_report-plugin
This %{oname} plugin provides spamreport.

%if %mdkversion > 200800
%package -n %{oname}-tnef_parse-plugin
Summary:        This plugin for %{oname} enables parsing MS-TNEF attachments
Group:          Networking/Mail
Requires:       %{oname} >= %{claws_version}
Provides:       sylpheed-claws2-tnef_parse-plugin
Obsoletes:      sylpheed-claws2-tnef_parse-plugin
Provides:       sylpheed-claws-tnef_parse-plugin
Obsoletes:      sylpheed-claws-tnef_parse-plugin

%description -n %{oname}-tnef_parse-plugin
This %{oname} plugin enables parsing MS-TNEF attachments
%endif

%prep
%setup -q -c

%build
cd claws-mail-extra-plugins-%{version}

%if %mdkversion <= 200800
rm -r tnef_parse*
%endif

mv ./* ../
cd -
rmdir claws-mail-extra-plugins-%{version}
#rm -rf CVS/ pgpinline/
for i in `find ./* -maxdepth 0  -type d`
    do
    cd $i
    #./autogen.sh
    %configure2_5x
    %make
    cd -
done

%install
rm -rf $RPM_BUILD_ROOT

CLAWS_MAIL_PLUGINDIR=$(pkg-config --variable=plugindir claws-mail)

for i in `find ./* -maxdepth 0  -type d`
    do
    cd $i
    %makeinstall_std CLAWS_MAIL_PLUGINDIR=$CLAWS_MAIL_PLUGINDIR
    cd -
done

# remove devel files from plugins
rm -rf ${RPM_BUILD_ROOT}/%{_libdir}/%{oname}/plugins/*.a
#CAE have to rm to prevent conflict libical-devel
#Handled upstream
#rm -f ${RPM_BUILD_ROOT}/%{_includedir}/ical.h

# fix permissions
chmod 644 vcalendar*/AUTHORS vcalendar*/COPYING vcalendar*/INSTALL vcalendar*/NEWS vcalendar*/README

%find_lang  %{oname}-acpi-plugin
%find_lang  %{oname}-gtkhtml2_viewer-plugin
%find_lang  %{oname}-vcalendar-plugin
%find_lang  %{oname}-rssyl-plugin
%find_lang  %{oname}-attachwarner-plugin
%find_lang  %{oname}-pdf_viewer-plugin
%find_lang  %{oname}-spam_report-plugin
%if %mdkversion > 200800
%find_lang  %{oname}-tnef_parse-plugin
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{oname}-acpi-plugin -f %{oname}-acpi-plugin.lang
%defattr(-,root,root)
%doc acpi*/AUTHORS
%doc acpi*/COPYING
%doc acpi*/ChangeLog
%doc acpi*/INSTALL
%doc acpi*/NEWS
%doc acpi*/README
%{_libdir}/%{oname}/plugins/acpi*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/acpi_notifier.mo


%files -n %{oname}-att_remover-plugin
%defattr(-,root,root)
%doc att_remover*/AUTHORS
%doc att_remover*/COPYING
%doc att_remover*/ChangeLog
%doc att_remover*/INSTALL
%doc att_remover*/NEWS
%doc att_remover*/README
%{_libdir}/%{oname}/plugins/att_remover*

%files -n %{oname}-attachwarner-plugin
%defattr(-,root,root)
%doc attachwarner*/AUTHORS
%doc attachwarner*/COPYING
%doc attachwarner*/ChangeLog
%doc attachwarner*/INSTALL
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/attachwarner*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/attach*.mo

%files -n %{oname}-cachesaver-plugin
%defattr(-,root,root)
%doc cachesaver*/AUTHORS
%doc cachesaver*/COPYING
%doc cachesaver*/ChangeLog
%doc cachesaver*/INSTALL
%{_libdir}/%{oname}/plugins/cachesaver*

%files -n %{oname}-fetchinfo-plugin
%defattr(-,root,root)
%doc fetchinfo*/COPYING
%doc fetchinfo*/ChangeLog
%doc fetchinfo*/INSTALL
%doc fetchinfo*/README
%{_libdir}/%{oname}/plugins/fetchinfo*

%files -n %{oname}-mailmbox-plugin
%defattr(-,root,root)
%doc mailmbox*/AUTHORS
%doc mailmbox*/COPYING
%doc mailmbox*/ChangeLog
%doc mailmbox*/INSTALL
%doc mailmbox*/README
%{_libdir}/%{oname}/plugins/mailmbox*

%files -n %{oname}-newmail-plugin
%defattr(-,root,root)
%doc newmail*/AUTHORS
%doc newmail*/COPYING
%doc newmail*/ChangeLog
%doc newmail*/INSTALL
%doc newmail*/NEWS
%doc newmail*/README
%{_libdir}/%{oname}/plugins/newmail*

%files -n %{oname}-notification-plugin
%defattr(-,root,root)
%doc notif*/AUTHORS
%doc notif*/COPYING
%doc notif*/ChangeLog
%doc notif*/INSTALL
%doc notif*/NEWS
%doc notif*/README
%{_libdir}/%{oname}/plugins/noti*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/notification_plugin.mo

%files -n %{oname}-perl-plugin
%defattr(-,root,root)
%doc perl*/AUTHORS
%doc perl*/COPYING
%doc perl*/ChangeLog
%doc perl*/INSTALL
%doc perl*/NEWS
%doc perl*/README
%doc perl*/cm_perl.pod
%{_libdir}/%{oname}/plugins/perl*

%files -n %{oname}-rssyl-plugin -f %{oname}-rssyl-plugin.lang
%doc rssyl*/AUTHORS
%doc rssyl*/COPYING
%doc rssyl*/ChangeLog
%doc rssyl*/INSTALL
%doc rssyl*/NEWS
%{_libdir}/%{oname}/plugins/rssyl*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/rssyl.mo

%files -n %{oname}-smime-plugin
%defattr(-,root,root)
%doc smim*/COPYING
%doc smim*/ChangeLog
%doc smim*/INSTALL
%doc smim*/NEWS
%doc smim*/README
%{_libdir}/%{oname}/plugins/smim*

%Files -n %{oname}-synce-plugin
%defattr(-,root,root)
%doc synce*/AUTHORS
%doc synce*/COPYING
%doc synce*/ChangeLog
%doc synce*/NEWS
%doc synce*/README
%{_libdir}/%{oname}/plugins/synce*

%files -n %{oname}-vcalendar-plugin
%defattr(-,root,root)
%doc vcalendar*/AUTHORS
%doc vcalendar*/COPYING
%doc vcalendar*/ChangeLog
%doc vcalendar*/INSTALL
%doc vcalendar*/NEWS
%doc vcalendar*/README
%{_libdir}/%{oname}/plugins/vcalendar*
%{_includedir}/ical.h
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/vcalendar.mo

%files -n %{oname}-gtkhtml2_viewer-plugin -f %{oname}-gtkhtml2_viewer-plugin.lang
%defattr(-,root,root)
%doc gtkhtml2*/AUTHORS
%doc gtkhtml2*/COPYING
%doc gtkhtml2*/ChangeLog
%doc gtkhtml2*/INSTALL
%doc gtkhtml2*/NEWS
%doc gtkhtml2*/README
%{_libdir}/%{oname}/plugins/gtkhtml2_viewer*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/gtkhtml2_viewer.mo

%files -n %{oname}-pdf_viewer-plugin -f %{oname}-pdf_viewer-plugin.lang
%defattr(-,root,root)
%{_libdir}/%{oname}/plugins/pdf_viewer*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/pdf_viewer.mo

%files -n %{oname}-spam_report-plugin -f %{oname}-spam_report-plugin.lang
%defattr(-,root,root)
%{_libdir}/%{oname}/plugins/spamreport*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/spam_report.mo

%if %mdkversion > 200800
%files -n %{oname}-tnef_parse-plugin -f %{oname}-tnef_parse-plugin.lang
%defattr(-,root,root)
%{_libdir}/%{oname}/plugins/tnef_parse*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/tnef_parse.mo
%endif

