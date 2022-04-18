create table customers
(
    CustomerID    bigint primary key,
    Name          varchar,
    Gender        varchar,
    PhoneNumber   bigint,
    Email         varchar,
    Address       varchar,
    "Postal Code" varchar,
    "User ID"     varchar,
    Password      varchar
);


create table booking
(
    BookingID    bigint primary key,
    CustomerID   bigint,
    DressID      bigint,
    Booking_Date bigint,
    Total_Amount bigint,
    Description  TEXT,
    CONSTRAINT fk_customer
        FOREIGN KEY (CustomerID)
            REFERENCES customers (CustomerID),
    CONSTRAINT fk_dress
        FOREIGN KEY (DressID)
            REFERENCES dress (DressID)
);


create table Payment
(
    PaymentId         bigint primary key,
    BookingID         bigint,
    Payment_Date_Time Date,
    Total_Amount      bigint,
    Status            varchar,
    CONSTRAINT fk_booking
        FOREIGN KEY (BookingID)
            REFERENCES booking (BookingID)
);

create table dress
(
    DressId     bigint primary key,
    StoreID     bigint,
    CategoryID  bigint,
    Name        varchar,
    size        varchar,
    color       varchar,
    Ideal_For   varchar,
    Rental_Rate bigint,
    Description TEXT,
    CONSTRAINT fk_StoreID
        FOREIGN KEY (StoreID)
            REFERENCES store (StoreID)
);

create table stock
(
    stockid    bigint primary key,
    DressId    bigint,
    dress_name varchar,
    quantity   varchar,
    CONSTRAINT fk_dressid
        FOREIGN KEY (DressId)
            REFERENCES dress (DressId)
);

create table store
(
    StoreID     bigint primary key,
    store_name  varchar,
    Phone_no    bigint,
    Email       varchar,
    Address     varchar,
    Postal_Code varchar
);