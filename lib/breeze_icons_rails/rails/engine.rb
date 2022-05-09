# frozen_string_literal: true

module BreezeIconsRails
  module Rails
    # add assets to rails pipeline
    class Engine < ::Rails::Engine
      initializer "breeze_icons_rails.assets" do |app|
        %w[stylesheets fonts].each do |sub|
          app.config.assets.paths << root.join("assets", sub).to_s
        end
      end
    end
  end
end
