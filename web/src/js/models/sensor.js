var app = app || {};

(function () {
    'use strict';

    // Sensor Model

    app.Sensor = Backbone.Model.extend({
        urlRoot: 'http://localhost:8000/api/v1/sensors',
        url: function() {
            return this.urlRoot + '?uuid=' + this.uuid;
        }
    });
})();