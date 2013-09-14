package com.appway.entity;

import java.util.Date;

public class CreditCardAccount extends Account {

	public Date expirationDate;

	public Date getExpirationDate() {
		return expirationDate;
	}

	public void setExpirationDate(Date expirationDate) {
		this.expirationDate = expirationDate;
	}

}