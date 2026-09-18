{{- /* The markdown companion for a page, served at <page>/index.md.

       .RawContent is the authored markdown with front matter stripped, so this is the
       essay as written rather than a reconstruction from rendered HTML. Only /posts/
       reaches this template: content/notes/_index.md cascades outputs to HTML for the
       2,521-note archive, and content/about.md pins itself to HTML because its body is
       about-role markup rather than prose. */ -}}
# {{ .Title }}

{{ with .Description }}> {{ . }}

{{ end -}}
{{- with .Date }}Published {{ .Format "2006-01-02" }}. {{ end }}Canonical: {{ .Permalink }}

---

{{ .RawContent }}
