# frozen_string_literal: true

require "breeze_icons_rails/rails/helpers"

module BreezeIconsRails
  module Rails
    class Railtie < ::Rails::Railtie
      initializer "breeze_icons_rails.view_helpers" do
        ActiveSupport.on_load(:action_view) do
          include BreezeIconsRails::Rails::ViewHelpers
        end
      end
    end
  end
end
