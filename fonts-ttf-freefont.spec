Summary:	A set of free Truetype fonts (GPL)
Name:		fonts-ttf-freefont
Version:	20120503
Release:	1
License:	GPLv3+
Group:		System/Fonts/True type
Url:		http://www.nongnu.org/freefont/
Source0:	http://ftp.gnu.org/gnu/freefont/freefont-ttf-%{version}.zip
Source1:	remove-kana-glyphs
Source2:	freefont-20040828.readme_kana.mdk
# (mpol) pfaedit is now fontforge
Patch0:		freefont-20040828.fontforge.patch
BuildArch:	noarch
BuildRequires:	fontconfig
Requires(post,postun):	mkfontdir
Requires(post,postun):	mkfontscale

%description 
A set of Truetype fonts released under the GPL.
This project aims to provide a set of free outline
(PostScript Type0, TrueType, OpenType...) fonts
covering the ISO 10646/Unicode UCS (Universal Character Set).
This package provides the Truetype fonts from that project.

%prep
%setup -qn freefont-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF

install -m644 *.ttf %{buildroot}%{_datadir}/fonts/TTF

%post
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%postun
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%files
%doc AUTHORS CREDITS ChangeLog README
%{_datadir}/fonts/TTF/*.ttf
