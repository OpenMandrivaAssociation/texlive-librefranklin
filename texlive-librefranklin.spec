Name:		texlive-librefranklin
Version:	64441
Release:	2
Summary:	LaTeX support for the Libre-Franklin family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/librefranklin
License:	lppl ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librefranklin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librefranklin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Libre Franklin is an interpretation and expansion based on the
1912 Morris Fuller Benton's classic, designed by Pablo
Impallari, Rodrigo Fuenzalida and Nhung Nguyen.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/librefranklin
%{_texmfdistdir}/fonts/vf/impallari/librefranklin
%{_texmfdistdir}/fonts/type1/impallari/librefranklin
%{_texmfdistdir}/fonts/tfm/impallari/librefranklin
%{_texmfdistdir}/fonts/opentype/impallari/librefranklin
%{_texmfdistdir}/fonts/map/dvips/librefranklin
%{_texmfdistdir}/fonts/enc/dvips/librefranklin
%doc %{_texmfdistdir}/doc/fonts/librefranklin

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
