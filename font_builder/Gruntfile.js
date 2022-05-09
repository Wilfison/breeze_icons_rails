module.exports = function (grunt) {
  "use strict";

  grunt.initConfig({
    webfont: {
      breeze_icons: {
        src: "./dist/*.svg",
        dest: "../docs",
        destScss: "../docs",
        options: {
          font: "Breeze Icons",
          fontFilename: "breeze-icons",
          skipLinks: true,
          engine: "fontforge",
          stylesheet: "scss",
          types: "ttf",
          order: "ttf",
          optimize: false,
          autoHint: false,
          templateOptions: {
            baseClass: "bi",
            classPrefix: "bi-",
          },
          htmlDemo: true,
          htmlDemoTemplate: "./demo.html",
          htmlDemoFilename: "index.html",
          destHtml: "../docs",
        },
      },
    },
  });

  grunt.loadNpmTasks("grunt-webfonts");

  // Run the default task by executing "grunt" in the CLI:
  grunt.registerTask("default", ["webfont"]);
};
