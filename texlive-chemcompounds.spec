%global tl_name chemcompounds
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Simple consecutive numbering of chemical compounds
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemcompounds
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The chemcompounds package allows for a simple consecutive numbering of
chemical compounds. Optionally, it is possible to supply a custom name
for each compound. The package differs from the chemcono package by not
generating an odd-looking list of compounds inside the text.

