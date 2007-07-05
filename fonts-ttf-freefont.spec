Summary:	A set of free Truetype fonts (GPL)
Name:		fonts-ttf-freefont
Version:	20060126
Release:	%mkrel 2

Source0:	freefont-ttf-%{version}.tar.gz
Source1:	remove-kana-glyphs
Source2:	freefont-20040828.readme_kana.mdk
# (mpol) pfaedit is now fontforge
Patch0:		freefont-20040828.fontforge.patch
License:	GPL
Group:		System/Fonts/True type
URL:		http://www.nongnu.org/freefont/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
Requires(post):	fontconfig
Requires(postun): fontconfig

%description 
A set of Truetype fonts released under the GPL.
This project aims to provide a set of free outline
(PostScript Type0, TrueType, OpenType...) fonts
covering the ISO 10646/Unicode UCS (Universal Character Set).
This package provides the Truetype fonts from that project.

%prep
%setup -q -n freefont-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

install -m644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache

%postun
if [ "$1" = "0" ]; then
	[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc AUTHORS CREDITS ChangeLog README
%{_datadir}/fonts/TTF/*.ttf
