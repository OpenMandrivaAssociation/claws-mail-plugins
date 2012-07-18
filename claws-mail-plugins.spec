%define oname claws-mail
%define cvs %nil
%define _disable_ld_no_undefined 1
%define claws_version %{version}

Summary:	This package contains additional plugins for %{oname}
Name:		%{oname}-plugins
Version:	3.8.1
Release:	1
Group:		Networking/Mail
License:	GPL
URL:		http://www.claws-mail.org/plugins/downloads
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{oname}-extra-plugins-%{version}%{cvs}.tar.bz2
Patch1:		claws-mail-plugins-3.7.10-perl.patch
Epoch:		1
BuildRequires:	claws-mail-devel = 1:%{claws_version}
BuildRequires:	claws-mail = 1:%{claws_version}
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	libetpan-devel
BuildRequires:	libytnef-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(libgtkhtml-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(librapi2)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(webkit-1.0)
Obsoletes:	%{oname}-cachesaver-plugin
Obsoletes:	%{oname}-synce-plugin
Requires:	%{oname} = %{claws_version}

%description
This package contains additional plugins for %{oname}:
%{oname}-acpi-plugin,
%{oname}-att_remover-plugin,
%{oname}-bsfilter-plugin,
%{oname}-fancy-plugin,
%{oname}-fetchinfo-plugin,
%{oname}-gdata-plugin,
%{oname}-mailmbox-plugin,
%{oname}-notification-plugin,
%{oname}-pdfviewer-plugin,
%{oname}-perl-plugin,
%{oname}-python-plugin,
%{oname}-rssyl-plugin,
%{oname}-vcalendar-plugin,
%{oname}-vcalendar-plugin-devel,
%{oname}-spamreport-plugin,
%{oname}-tnefparse-plugin

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

%package -n %{oname}-gdata-plugin
Summary:	This plugin enables access to GData (Google services)
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-gdata-plugin
Plugin to access to GData (Google services). The only currently implemented
feature is inclusion of Google contacts into the address completion.

%package -n %{oname}-gtkhtml2_viewer-plugin
Summary:	This plugin for %{oname} enables gtkhtml2 viewer
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws2-gtkhtml2_viewer-plugin < %{claws_version}
Provides:	sylpheed-claws-gtkhtml2_viewer-plugin
Obsoletes:	sylpheed-claws-gtkhtml2_viewer-plugin < %{claws_version}

%description -n %{oname}-gtkhtml2_viewer-plugin
This %{oname} plugin provides gtkhtml2 viewer.

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
Requires:	%{oname} >= %{claws_version}
Obsoletes:	sylpheed-claws-notification-plugin < %{claws_version}
Provides:	sylpheed-claws-notification-plugin

%description -n %{oname}-notification-plugin
This plugin for %{oname} notify from new incoming mail.

%package -n %{oname}-notification-plugin-devel
Summary:	This plugin for %{oname} install the notification plugin headers
Group:		Networking/Mail
Requires:	%{oname}-devel >= %{claws_version}

%description -n %{oname}-notification-plugin-devel
Header files for %{oname}-notification-plugin.

%package -n %{oname}-pdfviewer-plugin
Summary:	%{oname} plugin to handle PDF attachments
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}

%description -n %{oname}-pdfviewer-plugin
This %{oname} plugin This plugin handles PDF and Postscript attachments.

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

%package -n %{oname}-tnef_parse-plugin
Summary:	This plugin for %{oname} enables parsing MS-TNEF attachments
Group:		Networking/Mail
Requires:	%{oname} >= %{claws_version}
Provides:	sylpheed-claws2-tnef_parse-plugin
Obsoletes:	sylpheed-claws2-tnef_parse-plugin < %{claws_version}
Provides:	sylpheed-claws-tnef_parse-plugin
Obsoletes:	sylpheed-claws-tnef_parse-plugin < %{claws_version}

%description -n %{oname}-tnef_parse-plugin
This %{oname} plugin enables parsing MS-TNEF attachments.

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

%prep
%setup -q -n claws-mail-extra-plugins-%{version}
%patch1 -p1 -b .perl

%build
rm -r archive*
rm -r geolocation*

for i in `find ./* -maxdepth 0  -type d`
    do
    pushd $i
    #./autogen.sh
    %configure2_5x --disable-rpath --disable-static
    %make
    popd
done

%install
rm -rf %{buildroot}

CLAWS_MAIL_PLUGINDIR=$(pkg-config --variable=plugindir claws-mail)

for i in `find ./* -maxdepth 0  -type d`
    do
    pushd $i
    %makeinstall_std CLAWS_MAIL_PLUGINDIR=$CLAWS_MAIL_PLUGINDIR
    popd
done

# remove devel files from plugins
rm -rf %{buildroot}%{_libdir}/%{oname}/plugins/*.a
#CAE have to rm to prevent conflict libical-devel
rm -f %{buildroot}%{_includedir}/ical.h
rm -rf %{buildroot}%{_includedir}/notification_plugin
rm -f %{buildroot}%{_includedir}/claws-mail/plugins/vcalendar/ical.h

# fix permissions
chmod 644 vcalendar*/AUTHORS vcalendar*/COPYING vcalendar*/INSTALL vcalendar*/NEWS vcalendar*/README

%find_lang acpi_notifier
%find_lang address_keeper
%find_lang attachwarner
%find_lang bsfilter_plugin
%find_lang clamd
%find_lang fancy
%find_lang gdata_plugin
%find_lang gtkhtml2_viewer
%find_lang notification_plugin
%find_lang pdf_viewer
%find_lang python_plugin
%find_lang rssyl
%find_lang spam_report
%find_lang tnef_parse
%find_lang vcalendar

%files -n %{oname}-acpi-plugin -f acpi_notifier.lang
%doc acpi*/AUTHORS
%doc acpi*/ChangeLog
%doc acpi*/NEWS
%doc acpi*/README
%{_libdir}/%{oname}/plugins/acpi*

%files -n %{oname}-address_keeper-plugin -f address_keeper.lang
%doc address_keeper*/AUTHORS
%doc address_keeper*/ChangeLog
%{_libdir}/%{oname}/plugins/address_keeper*

%files -n %{oname}-att_remover-plugin
%doc att_remover*/AUTHORS
%doc att_remover*/ChangeLog
%doc att_remover*/NEWS
%doc att_remover*/README
%{_libdir}/%{oname}/plugins/att_remover*

%files -n %{oname}-attachwarner-plugin -f attachwarner.lang
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/attachwarner*

%files -n %{oname}-bsfilter-plugin -f bsfilter_plugin.lang
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/bsfilter*

%files -n %{oname}-clamd-plugin -f clamd.lang
%doc clamd*/AUTHORS
%doc clamd*/ChangeLog
%doc clamd*/README
%{_libdir}/%{oname}/plugins/clamd*

%files -n %{oname}-fancy-plugin -f fancy.lang
%doc attachwarner*/AUTHORS
%doc attachwarner*/ChangeLog
%doc attachwarner*/NEWS
%doc attachwarner*/README
%doc attachwarner*/TODO
%{_libdir}/%{oname}/plugins/fancy*

%files -n %{oname}-fetchinfo-plugin
%doc fetchinfo*/ChangeLog
%doc fetchinfo*/README
%{_libdir}/%{oname}/plugins/fetchinfo*

%files -n %{oname}-gdata-plugin -f gdata_plugin.lang
%doc gdata*/AUTHORS
%doc gdata*/ChangeLog
%doc gdata*/README
%{_libdir}/%{oname}/plugins/gdata*

%files -n %{oname}-gtkhtml2_viewer-plugin -f gtkhtml2_viewer.lang
%doc gtkhtml2*/AUTHORS
%doc gtkhtml2*/ChangeLog
%doc gtkhtml2*/NEWS
%doc gtkhtml2*/README
%{_libdir}/%{oname}/plugins/gtkhtml2_viewer*

%files -n %{oname}-mailmbox-plugin
%doc mailmbox*/AUTHORS
%doc mailmbox*/ChangeLog
%doc mailmbox*/README
%{_libdir}/%{oname}/plugins/mailmbox*

%files -n %{oname}-newmail-plugin
%doc newmail*/AUTHORS
%doc newmail*/ChangeLog
%doc newmail*/NEWS
%doc newmail*/README
%{_libdir}/%{oname}/plugins/newmail*

%files -n %{oname}-notification-plugin -f notification_plugin.lang
%doc notif*/AUTHORS
%doc notif*/ChangeLog
%doc notif*/NEWS
%doc notif*/README
%{_libdir}/%{oname}/plugins/noti*

%files -n %{oname}-notification-plugin-devel
%dir %{_includedir}/%{oname}/plugins/notification_plugin
%dir %{_includedir}/%{oname}/plugins/notification_plugin/gtkhotkey
%{_includedir}/%{oname}/plugins/notification_plugin/gtkhotkey/*.h

%files -n %{oname}-pdfviewer-plugin -f pdf_viewer.lang
%doc pdf_viewer*/AUTHORS
%doc pdf_viewer*/ChangeLog
%doc pdf_viewer*/README
%{_libdir}/%{oname}/plugins/pdf_viewer*

%files -n %{oname}-perl-plugin
%doc perl*/AUTHORS
%doc perl*/ChangeLog
%doc perl*/NEWS
%doc perl*/README
%doc perl*/cm_perl.pod
%{_libdir}/%{oname}/plugins/perl*

%files -n %{oname}-python-plugin -f python_plugin.lang
%doc python*/AUTHORS
%doc python*/ChangeLog
%doc python*/README
%{_libdir}/%{oname}/plugins/python*

%files -n %{oname}-rssyl-plugin -f rssyl.lang
%doc rssyl*/AUTHORS
%doc rssyl*/ChangeLog
%doc rssyl*/NEWS
%{_libdir}/%{oname}/plugins/rssyl*

%files -n %{oname}-spam_report-plugin -f spam_report.lang
%{_libdir}/%{oname}/plugins/spamreport*

%files -n %{oname}-tnef_parse-plugin -f tnef_parse.lang
%{_libdir}/%{oname}/plugins/tnef_parse*

%files -n %{oname}-vcalendar-plugin -f vcalendar.lang
%doc vcalendar*/AUTHORS
%doc vcalendar*/ChangeLog
%doc vcalendar*/NEWS
%doc vcalendar*/README
%{_libdir}/%{oname}/plugins/vcalendar*

%files -n %{oname}-vcalendar-plugin-devel
%{_includedir}/%{oname}/plugins/vcalendar/vcal_interface.h
