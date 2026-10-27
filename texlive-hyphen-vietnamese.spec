%global tl_name hyphen-vietnamese
%global tl_revision 74032

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	2
Summary:	Vietnamese hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-vietnamese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-vietnamese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Prevents hyphenation in Vietnamese.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-vietnamese:
vietnamese hyph-vi.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-vietnamese:
\addlanguage{vietnamese}{hyph-vi.tex}{}{0}{0}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-vietnamese:
['vietnamese'] = {
	loader = 'hyph-vi.tex',
	lefthyphenmin = 0,
	righthyphenmin = 0,
	synonyms = {  },
},
TL_HYPHEN_EOF
