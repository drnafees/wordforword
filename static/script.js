function filterLanguages(dropdownId) {
    const input = document.getElementById(dropdownId).parentElement.querySelector("input[type='text']");
    const filter = input.value.toUpperCase();
    const dropdownItems = document.getElementById(dropdownId).getElementsByClassName("dropdown-item");

    for (let i = 0; i < dropdownItems.length; i++) {
        const txtValue = dropdownItems[i].textContent || dropdownItems[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            dropdownItems[i].style.display = "";
        } else {
            dropdownItems[i].style.display = "none";
        }
    }
}

function selectLanguage(dropdownButtonId, code, name) {
    const fieldId = dropdownButtonId === 'sourceLanguageDropdown' ? 'source_language' : 'target_language';
    document.getElementById(fieldId).value = code;

    const dropdownButton = document.getElementById(dropdownButtonId);
    dropdownButton.textContent = name;

    const dropdownMenu = dropdownButton.nextElementSibling;
    dropdownMenu.classList.remove('show');
}
    