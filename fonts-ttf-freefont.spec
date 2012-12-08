Summary:	A set of free Truetype fonts (GPL)
Name:		fonts-ttf-freefont
Version:	20090104
Release:	%mkrel 7

Source0:	freefont-ttf-%{version}.tar.gz
Source1:	remove-kana-glyphs
Source2:	freefont-20040828.readme_kana.mdk
# (mpol) pfaedit is now fontforge
Patch0:		freefont-20040828.fontforge.patch
License:	GPLv3+
Group:		System/Fonts/True type
URL:		http://www.nongnu.org/freefont/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires: fontconfig
Requires(post): mkfontdir mkfontscale
Requires(postun): mkfontdir mkfontscale

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF

install -m644 *.ttf %{buildroot}%{_datadir}/fonts/TTF

%post
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%postun
mkfontscale %{_datadir}/fonts/TTF
mkfontdir %{_datadir}/fonts/TTF

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS CREDITS ChangeLog README
%{_datadir}/fonts/TTF/*.ttf


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 20090104-7mdv2011.0
+ Revision: 675417
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 20090104-6
+ Revision: 675181
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 20090104-5
+ Revision: 664329
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 20090104-4mdv2011.0
+ Revision: 605195
- rebuild

* Mon Mar 15 2010 Lev Givon <lev@mandriva.org> 20090104-3mdv2010.1
+ Revision: 519117
- Fix bug #57968.

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 20090104-2mdv2010.1
+ Revision: 494140
- fc-cache is now called by an rpm filetrigger

* Thu Jan 08 2009 Funda Wang <fwang@mandriva.org> 20090104-1mdv2009.1
+ Revision: 327126
- 20090104

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 20060126-3mdv2009.0
+ Revision: 220863
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060126-2mdv2008.1
+ Revision: 125126
- kill re-definition of %%buildroot on Pixel's request

  + Ademar de Souza Reis Jr <ademar@mandriva.com.br>
    - typo, cosmetic

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 20060126-2mdv2008.0
+ Revision: 48708
- fonts/TTF is already on fontpath, no need to
  call chkfontpath

* Mon Jul 02 2007 Funda Wang <fwang@mandriva.org> 20060126-1mdv2008.0
+ Revision: 46917
- New version


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:11:13 (52888)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:12:01 (52817)
- import fonts-ttf-freefont-20040828-4mdk

* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 20040828-4mdk
- Fix prereq
- don't package fontconfig cache

* Fri Sep 02 2005 Marcel Pol <mpol@mandriva.org> 20040828-3mdk
- fix requires

* Sat Aug 28 2004 Marcel Pol <mpol@mandrake.org> 20040828-2mdk
- add README_KANA.mdk with explanation why

* Sat Aug 28 2004 Marcel Pol <mpol@mandrake.org> 20040828-1mdk
- cvs update, build fonts from source
- remove KANA glyphs
- patch0, pfaedit is now fontforge

