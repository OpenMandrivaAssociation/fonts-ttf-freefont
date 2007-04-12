Summary:	A set of free Truetype fonts (GPL)
Name:		fonts-ttf-freefont
Version:	20040828
Release:	%mkrel 5

Source0:	freefont-%{version}.tar.bz2
Source1:	remove-kana-glyphs
Source2:	freefont-20040828.readme_kana.mdk
# (mpol) pfaedit is now fontforge
Patch0:		freefont-20040828.fontforge.patch
License:	GPL
Group:		System/Fonts/True type
URL:		http://www.nongnu.org/freefont/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
BuildRequires:	fontforge
Requires(post):	chkfontpath
Requires(post):	fontconfig
Requires(postun):fontconfig
Requires(postun): chkfontpath

%description 
A set of Truetype fonts released under the GPL.
This project aims to provide a set of free outline
(PostScript Type0, TrueType, OpenType...) fonts
covering the ISO 10646/Unicode UCS (Universal Character Set).
This package provides the Trueype fonts from that project.

%prep
%setup -q -c freefont
%patch0 -p1 -b .pfaedit

find . -name CVS -type d | xargs rm -rf

cp -f %{SOURCE1} freefont/tools/
cp -f %{SOURCE2} freefont/README_KANA.mdk


%build
cd freefont/sfd
# remove KANA glyphs to improve the appearance of Japanese (Suse)
../tools/remove-kana-glyphs *.sfd
../tools/ConvertFont *.sfd


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

cd freefont/sfd
install -m644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

%post
[ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -a %{_datadir}/fonts/TTF
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache

%postun
if [ "$1" = "0" ]; then
	[ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -r %{_datadir}/fonts/TTF
	[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc freefont/AUTHORS freefont/CREDITS freefont/ChangeLog freefont/README
%doc freefont/README_KANA.mdk
%{_datadir}/fonts/TTF/*.ttf



