/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    switch (typeof object) {
        case "object":
            if (Array.isArray(object)) {
                const elements = object.map((element) => jsonStringify(element));
                return `[${elements.join(',')}]`;
            } else if (object === null) {
                return "null";
            } else {
                const keys = Object.keys(object);
                const kv = keys.map((key) => `"${key}":${jsonStringify(object[key])}`);
                return `{${kv.join(',')}}`;
            }

        case "boolean":
        case "number":
            return object.toString();

        case "string":
            return `"${object}"`;

        default:
            return "";
    }
};
