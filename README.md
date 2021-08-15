  # Wapp-Chat-Data-Parsing-From-Text-Files
  This program is designed and implemented for parsing data and grouping information based on "message export" files of Whatsapp in .txt format.
Most of the code in the version V1.0 is focused on basic reading from a file, storing data in data structures and in general,
pracitising basic Python programming skills and applying "Thinking Pythonically" as quoted by Prof. Charles Severance in his "Python for Everybody" book.
In the following versions of the code, main concern will be centered of applying statistical operations on and visualizing the parsed data.
For the time being most of this functionality is left out to be handled by Microsoft Excel Spreadsheets.
Thank you for your interest and I hope this piece of simple coding project earns your, even partial, aprreciation.

!!!Program functionality is sensitive to data file format!!!
!!!Restrcitions about file format:
     *All message lines must start with a time stamp and then must be followed by the username, end with columns and a message body.
     e.g. [6.12.2019 02:27:10] Utku Turkbey: <message body>
     *Username might vary but time stamp format is strict
     *Only English alphabet letters are allowed, otherwise statistical values might be incorrect

Procedures mainly consist of:
     1)opening file,
     2)reading file and modifying necessary data structures wrt data,
     3)Printing results in a ordered and easy to read format
