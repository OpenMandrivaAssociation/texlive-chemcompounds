Name:		texlive-chemcompounds
Version:	15878
Release:	2
Summary:	Simple consecutive numbering of chemical compounds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemcompounds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The chemcompounds package allows for a simple consecutive
numbering of chemical compounds. Optionally, it is possible to
supply a custom name for each compound. The package differs
from the chemcono package by not generating an odd-looking list
of compounds inside the text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemcompounds/chemcompounds.sty
%doc %{_texmfdistdir}/doc/latex/chemcompounds/README
%doc %{_texmfdistdir}/doc/latex/chemcompounds/chemcompounds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chemcompounds/chemcompounds.dtx
%doc %{_texmfdistdir}/source/latex/chemcompounds/chemcompounds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
