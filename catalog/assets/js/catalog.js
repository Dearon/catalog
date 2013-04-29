function Entry(id, name, content) {
    var self = this;
    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.content = ko.observable(content);
}

function EntriesViewModel() {
    var self = this;
    self.csrftoken = getCookie('csrftoken');
    self.entries = ko.observableArray([]);
    self.entryID = ko.observable("");
    self.nameToAdd = ko.observable("");
    self.contentToAdd = ko.observable("");
    self.filter = ko.observable("");

    $.getJSON("/entries/", function(allEntries) {
        var mappedEntries = $.map(allEntries, function(entry) { return new Entry(entry.id, entry.name, entry.content) });
        self.entries(mappedEntries);
    });

    self.visibleEntries = ko.computed(function() {
        var filter = self.filter().toLowerCase();

        if (!filter) {
            return self.entries();
        } else {
            return ko.utils.arrayFilter(self.entries(), function(entry) {
                return stringStartsWith(entry.name().toLowerCase(), filter);
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

    self.showEditModal = function(entry) {
        self.entryID(entry.id());
        self.nameToAdd(entry.name());
        self.contentToAdd(entry.content());
        $('#editModal').modal('show');
    };
    
    self.editEntry = function() {
        if ((self.nameToAdd() != "") && (self.contentToAdd() != "")) {
            $.ajax({
                type: "POST",
                url: "/entries/edit/",
                data: { id: self.entryID, name: self.nameToAdd, content: self.contentToAdd },
                beforeSend: function(xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", self.csrftoken);
                },
                success: function(data) {
                    var entryID = self.entryID();

                    ko.utils.arrayForEach(self.entries(), function(entry) {
                        if (entry.id() == entryID) {
                            entry.name(data.name);
                            entry.content(data.content);
                        }
                    });

                    self.resetFields();
                    $('#editModal').modal('hide');
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
