DROP TABLE IF EXISTS province;
-- TODO 待完善
CREATE TABLE province(
    name VARCHAR(10) PRIMARY KEY,
    confirmed INTEGER(6),
    died INTEGER(6),
    crued INTEGER(6)
)