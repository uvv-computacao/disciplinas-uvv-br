source "https://rubygems.org"

# Versão do Jekyll a ser executada:
gem "jekyll"

# Temas disponíveis para serem utilizados:
gem "minima"
gem "just-the-docs"

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

# Outra gabiarra para aumentar a performance se
# estivermos usando Windows:
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Mantém a gem `http_parser.rb` na versão `v0.6.x`
# durante os builds do JRuby, já que novas versõe~s das gem
# não têm um  builds since newer versions of the gem
# não têm uma contrapartida Java:
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Usa a gem webrick para poder usar o servidor local
# durante o desenvolvimento:
gem "webrick", "~> 1.7"
