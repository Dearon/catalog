function Entry(id, name, content) {
    var self = this;
    self.id = id;
    self.name = name;
    self.content = content;
}

function EntriesViewModel() {
    var self = this;
    self.csrftoken = getCookie('csrftoken');
    self.entries = ko.observableArray([]);
    self.nameToAdd = ko.observable("");
    self.contentToAdd = ko.observable("");
    self.filter = ko.observable("");

    $.getJSON("/entries/", function(allEntries) {
        var mappedEntries = $.map(allEntries, function(entry) { return new Entry(entry.id, entry.name, entry.content) });
        self.entries(mappedEntries);
    });

    self.filteredEntries = ko.computed(function() {
        var filter = self.filter().toLowerCase();

        if (!filter) {
            return self.entries();
        } else {
            return ko.utils.arrayFilter(this.entries(), function(entry) {
                return stringStartsWith(entry.name.toLowerCase(), filter);
            });
        }
    }, this);

    self.resetFields = function() {
        self.nameToAdd("");
        self.contentToAdd("");
    };

    self.addEntry = function() {
        if ((self.nameToAdd() != "") && (self.contentToAdd() != "")) {
            $.ajax({
                type: "POST",
                url: "/entries/add/",
                data: { name: self.nameToAdd, content: self.contentToAdd },
                beforeSend: function(xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", self.csrftoken);
                },
                success: function(data) {
                    self.entries.push(new Entry(data.id, data.name, data.content));
                    self.resetFields();
                    $('#newModal').modal('hide');
                }
            });

        }
    };

    self.removeEntry = function(entry) {
        $.ajax({
            type: "POST",
            url: "/entries/remove/",
            data: { id: entry.id },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", self.csrftoken);
            },
            success: function(data) {
                self.entries.destroy(entry);
            }
        });
    }
}

ko.applyBindings(new EntriesViewModel());
