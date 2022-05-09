![feathericon](https://raw.githubusercontent.com/Wilfison/breeze_icons_rails/master/docs/breeze-icons.png "feathericon")

<h1 align="center">Breeze Icons Rails</h1>
<p align="center">Breeze Icons for Rails Projects</p>
<!-- <div align="center">
  <a href="https://rubygems.org/gems/breeze_icons_rails">
    <img src="http://img.shields.io/gem/v/breeze_icons_rails.svg" alt="Gem Version">
  </a>
  <a href="https://rubygems.org/gems/breeze_icons_rails">
    <img src="https://img.shields.io/gem/dt/breeze_icons_rails.svg" alt="Gem Downloads">
  </a>
</div> -->

<p align="center">Icons: <a href="https://wilfison.github.io/breeze_icons_rails/">wilfison.github.io/breeze_icons_rails</a></p>

## Usage

Place Breeze Icons with `<i>` tag in your html like this. `bi` class is required to use our icons correctly. Check out [icons page](https://wilfison.github.io/breeze_icons_rails/) to start using icons!

*HTML*
```html
<i class="bi bi-list-add"></i>
```

*ERB*
```erb
<%= bi_icon 'list-add' %>
```

*HAML*
```haml
= bi_icon 'list-add'
```

## Installation
Add this line to your application's Gemfile:

```ruby
gem 'breeze_icons_rails'
```

And then execute:
```bash
$ bundle
```

Or install it yourself as:
```bash
$ gem install breeze_icons_rails
```

## Require

Add this line to your `app/assets/stylesheets/application.scss`:
```scss
@import 'breeze-icons';
```

## License
The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
