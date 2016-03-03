var app = app || {};

(function ($) {
    'use strict';

    app.SensorView = Backbone.View.extend({

        template: _.template($('#sensor-template').html()),

        initialize: function() {
            this.listenTo(this.model, 'change', this.render);
        },

        render: function() {
            this.$el.html(this.template(this.model.attributes));
        }
    });
})(jQuery);