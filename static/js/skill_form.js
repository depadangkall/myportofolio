function setupSkillLogoField(form) {
    if (!form) return;

    const categorySelect = form.querySelector('select[name="category"]');
    const logoInput = form.querySelector('input[name="logo"]');
    if (!categorySelect || !logoInput) return;

    const logoGroup = logoInput.closest('.form-group');

    function toggleLogoField() {
        const isSoftSkill = categorySelect.value === 'soft';
        logoGroup.classList.toggle('hide', isSoftSkill);
        if (isSoftSkill) logoInput.value = '';
    }

    categorySelect.addEventListener('change', toggleLogoField);
    form.addEventListener('reset', () => setTimeout(toggleLogoField));
    toggleLogoField();
}
