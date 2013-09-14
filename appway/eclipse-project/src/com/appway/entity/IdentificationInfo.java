package com.appway.entity;

public class IdentificationInfo {

	public String identificationString;

	public Integer type;

	public Integer id;
	
	public IdentificationInfo() {
		super();
	}
	
	public IdentificationInfo(String i, Integer t, Integer id) {
		super();
		this.identificationString = i;
		this.type = t;
		this.id = id;
	}
	

	public String getIdentificationString() {
		return identificationString;
	}

	public void setIdentificationString(String identificationString) {
		this.identificationString = identificationString;
	}

	public Integer getType() {
		return type;
	}

	public void setType(Integer type) {
		this.type = type;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

}