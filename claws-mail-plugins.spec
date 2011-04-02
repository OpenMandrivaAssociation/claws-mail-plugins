%define oname claws-mail
%define claws_version 3.7.8
%define cvs %nil
%define _disable_ld_no_undefined 1

Summary:	This package contains additional plugins for %{oname}
Name:		%{oname}-plugins
Version:	%{claws_version}
Release:	%mkrel 1
Group:		Networking/Mail
License:	GPL
URL:		http://www.claws-mail.org/plugins/downloads
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{oname}-extra-plugins-%{version}%{cvs}.tar.bz2
Epoch:		1
BuildRequires:	claws-mail-devel = 1:%{claws_version}
BuildRequires:	claws-mail = 1:%{claws_version}
BuildRequires:	libetpan-devel
BuildRequires:	perl-devel
BuildRequires:	curl-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libgtkhtml2-devel
BuildRequires:	librapi-devel
BuildRequires:	ghostscript
BuildRequires:	pygtk2.0-devel
Obsoletes:	%{oname}-cachesaver-plugin
Obsoletes:	%{oname}-synce-plugin
Requires:	%{oname} = %{claws_version}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains additional plugins for %{oname}:
%{oname}-acpi-plugin,
%{oname}-att_remover-plugin,
%{oname}-bsfilter-plugin,
%{oname}-fancy-plugin,
%{oname}-fetchinfo-plugin,
%{oname}-mailmbox-plugin,
%{oname}-notification-plugin,
%{oname}-perl-plugin,
%{oname}-python-plugin,
%{oname}-rssyl-plugin,
%{oname}-vcalendar-plugin,
%{oname}-vcalendar-plugin-devel,
%{oname}-spamreport-plugin,
%{oname}-tnefparse-plugin,

%package -n %{oname}-acpi-plugin
Summary:	This plugin enables mail notification via LEDs on some laptops
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-acpi-plugin < %{claws_version}
Provides:	sylpheed-claws-acpi-plugin

%description -n %{oname}-acpi-plugin
This plugin for %{oname} enables mail notification via LEDs
on some laptops.

%package -n %{oname}-address_keeper-plugin
Summary:	This plugin for %{oname} never forget e-mail adresses
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-address_keeper-plugin
This plugin for %{oname} allows saving outgoing addresses to a designated
folder in the address book.Addresses are saved only if not found in the
address book to avoid unwanted duplicates.

%package -n %{oname}-att_remover-plugin
Summary:	This plugin for %{oname} enables the removal of attachments
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-att_remover-plugin < %{claws_version}
Provides:	sylpheed-claws-att_remover-plugin

%description -n %{oname}-att_remover-plugin
This plugin for %{oname} enables the removal of attachments.

%package -n %{oname}-bsfilter-plugin
Summary:	This plugin enables spam fitering through bsfilter
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-bsfilter-plugin
Check all messages that are received from an IMAP, LOCAL or POP account 
for spam using Bsfilter.

%package -n %{oname}-clamd-plugin
Summary:	This plugin enables spam fitering through Clam AntiVirus
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-clamd-plugin
Check all messages that are received from an IMAP, LOCAL or POP account 
for spam using Clam AntiVirus.

%package -n %{oname}-fancy-plugin
Summary:	This plugin renders HTML e-mails through WebKit
Group:		Networking/Mail
BuildRequires:	webkitgtk-devel
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-fancy-plugin
Renders HTML e-mail using the WebKit library 

%package -n %{oname}-fetchinfo-plugin
Summary:	This plugin inserts headers containing some download information
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-fetchinfo-plugin
Obsoletes:	sylpheed-claws2-fetchinfo-plugin < %{claws_version}
Provides:	sylpheed-claws-fetchinfo-plugin
Obsoletes:	sylpheed-claws-fetchinfo-plugin < %{claws_version}

%description -n %{oname}-fetchinfo-plugin
This plugin for %{oname} inserts headers containing some download
information: UIDL, Sylpheeds account name, POP server, user ID
and retrieval time.

%package -n %{oname}-mailmbox-plugin
Summary:	This plugin provides direct access to mbox folders
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-mailmbox-plugin
Obsoletes:	sylpheed-claws2-mailmbox-plugin < %{claws_version}
Provides:	sylpheed-claws-mailmbox-plugin
Obsoletes:	sylpheed-claws-mailmbox-plugin < %{claws_version}

%description -n %{oname}-mailmbox-plugin
This plugin for %{oname} provides direct access to mbox folders.

%package -n %{oname}-newmail-plugin
Summary:	This plugin can write a summary to a log file
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-newmail-plugin < %{claws_version}
Provides:	sylpheed-claws-newmail-plugin

%description -n %{oname}-newmail-plugin
This plugin for %{oname} can write a summary to a log file upon
receiving new mail. It defaults to ~/Mail/NewLog.

%package -n %{oname}-notification-plugin
Summary:	This plugin notify from new mail
Group:		Networking/Mail
BuildRequires:	libnotify-devel
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-notification-plugin < %{claws_version}
Provides:	sylpheed-claws-notification-plugin

%description -n %{oname}-notification-plugin
This plugin for %{oname} notify from new incoming mail.

%package -n %{oname}-perl-plugin
Summary:	Perl interface to %{oname}s' filtering mechanism
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-perl-plugin
Obsoletes:	sylpheed-claws2-perl-plugin < %{claws_version}
Provides:	sylpheed-claws-perl_plugin-plugin
Obsoletes:	sylpheed-claws-perl_plugin-plugin < %{claws_version}

%description -n %{oname}-perl-plugin
This plugin is intended to extend the filtering possibilities
of %{oname}. It provides a Perl interface to %{oname}s'
filtering mechanism, allowing the use of full Perl power in
email filters.

%package -n %{oname}-python-plugin
Summary:	Python scriptin access to %{oname}
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-python-plugin
This plugin offers a Python scripting access to %{oname}.

%package -n %{oname}-rssyl-plugin
Summary:	This plugin allows you to read your favorite newsfeeds in %{oname}
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-rssyl-plugin < %{claws_version}
Provides:	sylpheed-claws-rssyl-plugin

%description -n %{oname}-rssyl-plugin
This plugin allows you to read your favorite newsfeeds in %{oname}.
RSS 1.0, 2.0 and Atom feeds are currently supported.

%package -n %{oname}-vcalendar-plugin
Summary:	This plugin for %{oname} enables vCalendar message handling
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-vcalendar-plugin
Obsoletes:	sylpheed-claws2-vcalendar-plugin < %{claws_version}
Provides:	sylpheed-claws-vcalendar-plugin
Obsoletes:	sylpheed-claws-vcalendar-plugin < %{claws_version}

%description -n %{oname}-vcalendar-plugin
This %{oname} plugin handles the vCalendar format (or rather, the
meeting subset of it). It displays such mails in a nice format, lets you
create and send meetings, and creates a virtual folder with the meetings you
have sent or received.

%package -n %{oname}-vcalendar-plugin-devel
Summary:	This plugin for %{oname} install the vcalendar plugin headers 
Group:		Networking/Mail
Requires:	%{oname}-devel >= %{claws_version}

%description -n %{oname}-vcalendar-plugin-devel
Header files for %{oname}-vcalendar-plugin.

%package -n %{oname}-gtkhtml2_viewer-plugin
Summary:	This plugin for %{oname} enables gtkhtml2 viewer
Group:		Networking/Mail
BuildRequires:	gail-devel
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws2-gtkhtml2_viewer-plugin < %{claws_version}
Provides:	sylpheed-claws-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws-gtkhtml2_viewer-plugin < %{claws_version}

%description -n %{oname}-gtkhtml2_viewer-plugin
This %{oname} plugin provides gtkhtml2 viewer.

%package -n %{oname}-attachwarner-plugin
Summary:	This plugin for %{oname} enables attachwarner
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws2-gtkhtml2_viewer-plugin < %{claws_version}
Provides:	sylpheed-claws-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws-gtkhtml2_viewer-plugin < %{claws_version}

%description -n %{oname}-attachwarner-plugin
This %{oname} plugin provides attachwarner.

%package -n %{oname}-spam_report-plugin
Summary:	This plugin for %{oname} enables spamreport
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-spam_report-plugin
Obsoletes:	sylpheed-claws2-spam_report-plugin < %{claws_version}
Provides:	sylpheed-claws-spam_report-plugin
Obsoletes:	sylpheed-claws-spam_report-plugin < %{claws_version}

%description -n %{oname}-spam_report-plugin
This %{oname} plugin provides spamreport.

%if %mdkversion > 200800
%package -n %{oname}-tnef_parse-plugin
Summary:	This plugin for %{oname} enables parsing MS-TNEF attachments
Group:		Networking/Mail
BuildRequires:	libytnef-devel
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-tnef_parse-plugin
Obsoletes:	sylpheed-claws2-tnef_parse-plugin < %{claws_version}
Provides:	sylpheed-claws-tnef_parse-plugin
Obsoletes:	sylpheed-claws-tnef_parse-plugin < %{claws_version}

%description -n %{oname}-tnef_parse-plugin
This %{oname} plugin enables parsing MS-TNEF attachments.
%endif

%prep
%setup -q -c

%build
cd claws-mail-extra-plugins-%{version}

%if %mdkversion <= 200800
rm -r tnef_parse*
%endif
rm -r archive*
rm -r geolocation*

mv ./* ../
cd -
rmdir claws-mail-extra-plugins-%{version}
#rm -rf CVS/ pgpinline/
for i in `find ./* -maxdepth 0  -type d`
    do
    cd $i
    #./autogen.sh
    %configure2_5x --disable-rpath --disable-static
    %make
    cd -
done

%install
rm -rf %{buildroot}

CLAWS_MAIL_PLUGINDIR=$(pkg-config --variable=plugindir claws-mail)

for i in `find ./* -maxdepth 0  -type d`
    do
    cd $i
    %makeinstall_std CLAWS_MAIL_PLUGINDIR=$CLAWS_MAIL_PLUGINDIR
    cd -
done

# remove devel files from plugins
rm -rf %{buildroot}%{_libdir}/%{oname}/plugins/*.a
#CAE have to rm to prevent conflict libical-devel
rm -f %{buildroot}%{_includedir}/ical.h
rm -rf %{buildroot}%{_includedir}/notification_plugin
rm -f %{buildroot}%{_includedir}/claws-mail/plugins/vcalendar/ical.h

# fix permissions
chmod 644 vcalendar*/AUTHORS vcalendar*/COPYING vcalendar*/INSTALL vcalendar*/NEWS vcalendar*/README

%find_lang  %{oname}-acpi-plugin
%find_lang  %{oname}-address_keeper-plugin
%find_lang  %{oname}-bsfilter-plugin
%find_lang  %{oname}-clamd-plugin
%find_lang  %{oname}-fancy-plugin
%find_lang  %{oname}-gtkhtml2_viewer-plugin
%find_lang  %{oname}-vcalendar-plugin
%find_lang  %{oname}-rssyl-plugin
%find_lang  %{oname}-attachwarner-plugin
%find_lang  %{oname}-spam_report-plugin
%if %mdkversion > 200800
%find_lang  %{oname}-tnef_parse-plugin
%endif

%clean
rm -rf %{buildroot}

%files -n %{oname}-acpi-plugin -f %{oname}-acpi-plugin.lang
%defattr(-,root,root)
%doc acpi*/AUTHORS
%doc acpi*/ChangeLog
%doc acpi*/NEWS
%doc acpi*/README
%{_libdir}/%{oname}/plugins/acpi*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/acpi_notifier.mo

%files -n %{oname}-address_keeper-plugin -f %{oname}-address_keeper-plugin.lang
%defattr(-,root,root)
%doc address_keeper*/AUTHORS
%doc address_keeper*/ChangeLog
%{_libdir}/%{oname}/plugins/address_keeper*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/address_keeper.mo

%files -n %{oname}-att_remover-plugin
%defattr(-,root,root)
%doc att_remover*/AUTHORS
%doc att_remover*/ChangeLog
%doc att_remover*/NEWS
%doc att_remover*/README
%{_libdir}/%{oname}/plugins/att_remover*

%files -n %{oname}-attachwarner-plugin
%defattr(-,root,root)
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/attachwarner*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/attach*.mo

%files -n %{oname}-bsfilter-plugin -f %{oname}-bsfilter-plugin.lang
%defattr(-,root,root)
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/bsfilter*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/bsfilter_plugin.mo

%files -n %{oname}-clamd-plugin -f %{oname}-clamd-plugin.lang
%defattr(-,root,root)
%doc clamd*/AUTHORS
%doc clamd*/ChangeLog
%doc clamd*/README
%{_libdir}/%{oname}/plugins/clamd*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/clamd.mo

%files -n %{oname}-fancy-plugin -f %{oname}-fancy-plugin.lang
%defattr(-,root,root)
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/fancy*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/fancy.mo

%files -n %{oname}-fetchinfo-plugin
%defattr(-,root,root)
%doc fetchinfo*/ChangeLog
%doc fetchinfo*/README
%{_libdir}/%{oname}/plugins/fetchinfo*

%files -n %{oname}-mailmbox-plugin
%defattr(-,root,root)
%doc mailmbox*/AUTHORS
%doc mailmbox*/ChangeLog
%doc mailmbox*/README
%{_libdir}/%{oname}/plugins/mailmbox*

%files -n %{oname}-newmail-plugin
%defattr(-,root,root)
%doc newmail*/AUTHORS
%doc newmail*/ChangeLog
%doc newmail*/NEWS
%doc newmail*/README
%{_libdir}/%{oname}/plugins/newmail*

%files -n %{oname}-notification-plugin
%defattr(-,root,root)
%doc notif*/AUTHORS
%doc notif*/ChangeLog
%doc notif*/NEWS
%doc notif*/README
%{_libdir}/%{oname}/plugins/noti*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/notification_plugin.mo

%files -n %{oname}-perl-plugin
%defattr(-,root,root)
%doc perl*/AUTHORS
%doc perl*/ChangeLog
%doc perl*/NEWS
%doc perl*/README
%doc perl*/cm_perl.pod
%{_libdir}/%{oname}/plugins/perl*

%files -n %{oname}-python-plugin
%defattr(-,root,root)
%doc perl*/AUTHORS
%doc perl*/ChangeLog
%doc perl*/README
%{_libdir}/%{oname}/plugins/python*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/python_plugin.mo

%files -n %{oname}-rssyl-plugin -f %{oname}-rssyl-plugin.lang
%doc rssyl*/AUTHORS
%doc rssyl*/ChangeLog
%doc rssyl*/NEWS
%{_libdir}/%{oname}/plugins/rssyl*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/rssyl.mo

%files -n %{oname}-vcalendar-plugin
%defattr(-,root,root)
%doc vcalendar*/AUTHORS
%doc vcalendar*/ChangeLog
%doc vcalendar*/NEWS
%doc vcalendar*/README
%{_libdir}/%{oname}/plugins/vcalendar*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/vcalendar.mo

%files -n %{oname}-vcalendar-plugin-devel
%defattr(-,root,root)
%{_includedir}/%{oname}/plugins/vcalendar/vcal_interface.h

%files -n %{oname}-gtkhtml2_viewer-plugin -f %{oname}-gtkhtml2_viewer-plugin.lang
%defattr(-,root,root)
%doc gtkhtml2*/AUTHORS
%doc gtkhtml2*/ChangeLog
%doc gtkhtml2*/NEWS
%doc gtkhtml2*/README
%{_libdir}/%{oname}/plugins/gtkhtml2_viewer*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/gtkhtml2_viewer.mo

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
