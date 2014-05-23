
/* from: http://stackoverflow.com/questions/3841441/oracle-how-to-insert-if-a-row-doesnt-exist */

INSERT INTO table
SELECT 'jonny', NULL
  FROM dual -- Not Oracle? No need for dual, drop that line
 WHERE NOT EXISTS (SELECT NULL -- canonical way, but you can select
                               -- anything as EXISTS only checks existence
                     FROM table
                    WHERE name = 'jonny'
                  );
