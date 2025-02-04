source "https://rubygems.org"

# Versão do Jekyll a ser executada:
gem "jekyll", "~> 4.4.1"
#gem "jekyll", "~> 4.3.2"

# Temas disponíveis para serem utilizados:
#gem "minima", "~> 2.5"
gem "just-the-docs", "0.10.1"

# Plugins a serem ativados:
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Windows (sempre ele!) não tem arquivos "zoneinfo",
# entao vamos agregar tudo com a gem tzinfo-data e
# outras bibliotecas associadas:
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# "Performance-booster" para monitorar diretórios
# ao usar Windows:
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Mantém a gem `http_parser.rb` na versão `v0.6.x`
# durante os builds do JRuby, já que novas versõe~s das gem
# não têm um  builds since newer versions of the gem
# não têm uma contrapartida Java:
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Usa a gem webrick para poder usar o servidor local
# durante o desenvolvimento:
gem "webrick", "~> 1.9"

# Usar o CodeRay syntax highlighter com o Kramdown:
gem "kramdown-syntax-coderay", "~> 1.0"

# Outras gems:
gem "csv"
gem "base64"
