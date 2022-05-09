# frozen_string_literal: true

require_relative "lib/breeze_icons_rails/version"

Gem::Specification.new do |spec|
  spec.name          = "breeze_icons_rails"
  spec.version       = BreezeIconsRails::VERSION
  spec.authors       = ["wilfison"]
  spec.email         = ["wilfisonbatista@gmail.com"]

  spec.summary       = "Breeze Icons for Ruby on Rails"
  spec.description   = "Simple, scalable vector icon font for websites, apps."
  spec.homepage      = "https://github.com/Wilfison/breeze_icons_rails"
  spec.license       = "MIT"

  spec.required_ruby_version = Gem::Requirement.new(">= 2.3.0")

  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = spec.homepage

  spec.files = Dir["{app,config,db,lib}/**/*", "LICENSE", "Rakefile", "README.md"]

  spec.require_paths = ["lib"]
end
