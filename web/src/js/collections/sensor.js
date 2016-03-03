var app = app || {};

(function () {
    'use strict';

    // Sensor Collection

    var Sensors = Backbone.Collection.extend({
        // Reference this collection's model.
        model: app.Sensor,


    });

    // Create our global collection of **Sensors**.
    app.sensors = new Sensors();
})();