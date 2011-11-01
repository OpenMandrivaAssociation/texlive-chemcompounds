Name:		texlive-chemcompounds
Version:	20070305
Release:	1
Summary:	Simple consecutive numbering of chemical compounds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemcompounds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The chemcompounds package allows for a simple consecutive
numbering of chemical compounds. Optionally, it is possible to
supply a custom name for each compound. The package differs
from the chemcono package by not generating an odd-looking list
of compounds inside the text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
