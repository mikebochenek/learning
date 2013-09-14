package com.appway.entity;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Client {

	public Integer id;

	public Date dateOfEntry;

	public IdentificationInfo identification;
	
	public List<Address> addressList;
	
	public List<Account> accountList;
	
	/**
	 * 1. A function to retreive the first address of the client
	 * @return
	 */
	public Address getFirstAddress() {
		return (addressList == null || addressList.size() == 0) ? null : addressList.get(0);
	}
	
	/**
	 * 2. A function to retreive all the Checking accounts for the client
	 * @return
	 */
	public List<CheckingAccount> getAllCheckingAccounts() {
		List<CheckingAccount> cList = new ArrayList<CheckingAccount>();
		
		for (Account account : accountList) {
			if (account instanceof CheckingAccount) { // forgot to add a type attribute to Account class, so I have to do instanceof..
				cList.add((CheckingAccount) account);
			}
		}
		
		return cList;
	}

	/**
	 * 3. A function that copies the identification infromation from one client to another
	 * @param client
	 */
	public void cloneIdentificationInfo(Client client) {
		if (client.getIdentification() != null) {
			IdentificationInfo info = new IdentificationInfo(client.getIdentification().getIdentificationString(), client.getIdentification().getType(), client.getIdentification().getId());
			this.setIdentification(info);
		}
	}
	
	/**
	 * 4. (bonus) take the function specified as es.#2 and make it generic, allowing one to specify
	 * the type of account to be returned as an input parameter
	 * @param type
	 * @return
	 */
	public List<? extends Account> getAccounts(Class c) {
		List<Account> aList = new ArrayList<Account>();
		
		
		for (Account account : accountList) {
			if (c.isInstance(account)) { // forgot to add a type attribute to Account class, so I have to do instanceof..
				aList.add(account);
			}
		}

		return aList;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Date getDateOfEntry() {
		return dateOfEntry;
	}

	public void setDateOfEntry(Date dateOfEntry) {
		this.dateOfEntry = dateOfEntry;
	}

	public IdentificationInfo getIdentification() {
		return identification;
	}

	public void setIdentification(IdentificationInfo identification) {
		this.identification = identification;
	}

	public List<Address> getAddress() {
		return addressList;
	}

	public void setAddress(List<Address> address) {
		this.addressList = address;
	}

	public List<Account> getAccount() {
		return account;
	}

	public void setAccount(List<Account> account) {
		this.account = account;
	}

	public List<Account> account;

}
