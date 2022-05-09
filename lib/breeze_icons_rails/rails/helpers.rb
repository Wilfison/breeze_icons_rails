# frozen_string_literal: true

module BreezeIconsRails
  module Rails
    # add bi_icon helper
    module ViewHelpers
      def bi_icon(name, html_options = {})
        content_class = "bi bi-#{name}"
        content_class << " #{html_options[:class]}" if html_options.key?(:class)
        html_options[:class] = content_class
        html_options["aria-hidden"] ||= true

        content_tag(:i, nil, html_options)
      end
    end
  end
end
