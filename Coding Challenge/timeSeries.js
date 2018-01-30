process.stdin.resume();
process.stdin.setEncoding("ascii");

let input = "";

process.stdin.on("data", function (chunk) {
    input += chunk;
});

process.stdin.on("end", function () {
    let data = {};
    let lines = input.split("\n");

    // parse input data into data structure
    populateData(lines, data);
    
    // print out data
    stringify(data);
});

/**
 * Returns the start and end dates in the given line.
 *
 * @param line
 * @returns {{startDate: string, endDate: string}}
 */
function getDateInterval(line) {
    let startDate = line.substr(0, line.indexOf(',')).trim();
    let endDate = line.substr(line.indexOf(',') + 1).trim();

    return { startDate, endDate };
}

/**
 * Check if date is within the given time interval.
 *
 * @param date: given date
 * @param startDate: starting date
 * @param endDate: ending date
 * @returns {boolean}
 */
function isDateInInterval(date, startDate, endDate) {
    return startDate <= date && date <= endDate;
}

/**
 * Extract date from given string and return in YYYY-MM-DD format.
 *
 * @param str: the given string whose date should to be extracted.
 * @returns {string}
 */
function getFullDate(str) {
    return str.substr(0, str.indexOf(',')).trim();
}

/**
 * Extract short date, engagement, and count from the given line.
 * 
 * @param str
 * @returns {{date: string, engagement: string, count: string}}
 */
function getInfo(str) {
    let [fullDate, engagement, count] = str.split(", ");

    return { date: fullDate.substr(0, 7), engagement, count };
}

/**
 * Populate the time series data structure.
 * 
 * @param lines: strings containing data to populate data structure
 * @param data: time series data structure
 */
function populateData(lines, data) {
    // get interval dates
    let firstLine = lines.shift();
    let { startDate, endDate } = getDateInterval(firstLine);

    // remove empty second line
    lines.shift();
    
    for (let line of lines) {
        // process all dates within time interval
        if (isDateInInterval(getFullDate(line), startDate, endDate)) {
            let { date, engagement, count } = getInfo(line);

            // init new date
            if (!data.hasOwnProperty(date)) {
                data[date] = {};
            }

            // init new engagement or aggregate existing
            data[date].hasOwnProperty(engagement)
                ? data[date][engagement] = +count + +data[date][engagement]
                : data[date][engagement] = count;
        }
    }
}

/**
 * Stringify and print out the given time series data structure.
 * 
 * @param data: data structure that should be printed out.
 */
function stringify(data) {
    let output = "";
    
    // traverse dates starting from most recent
    let dates = Object.keys(data).sort().reverse();
    for (let date of dates) {
        output = output + date;

        // traverse engagements in alphabetical order
        let engagements = Object.keys(data[date]).sort();
        for (let engagement of engagements) {
            output = output + ", " + engagement + ", " + data[date][engagement];
        }

        output += "\n";
    }
    
    console.log(output);
}
