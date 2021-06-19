import { wrapFunctional } from './utils'

export { default as Footer } from '../../components/Footer.vue'
export { default as Navbar } from '../../components/Navbar.vue'
export { default as PartnersHowItWork } from '../../components/partners/HowItWork.vue'
export { default as PartnersHowItWorkVar } from '../../components/partners/HowItWorkVar.vue'
export { default as StoragesCardEdit } from '../../components/storages/CardEdit.vue'
export { default as StoragesCardOrder } from '../../components/storages/CardOrder.vue'
export { default as StoragesSearchResultItem } from '../../components/storages/SearchResultItem.vue'
export { default as SharedAccount } from '../../components/shared/Account.vue'
export { default as SharedAddingFile } from '../../components/shared/AddingFile.vue'
export { default as SharedCheckbox } from '../../components/shared/Checkbox.vue'
export { default as SharedCoreArea } from '../../components/shared/CoreArea.vue'
export { default as SharedCoreButton } from '../../components/shared/CoreButton.vue'
export { default as SharedCoreCheckbox } from '../../components/shared/CoreCheckbox.vue'
export { default as SharedCoreInput } from '../../components/shared/CoreInput.vue'
export { default as SharedDefaultArea } from '../../components/shared/DefaultArea.vue'
export { default as SharedDefaultButton } from '../../components/shared/DefaultButton.vue'
export { default as SharedDefaultInput } from '../../components/shared/DefaultInput.vue'
export { default as SharedDropDownFilter } from '../../components/shared/DropDownFilter.vue'
export { default as SharedIcoTitle } from '../../components/shared/IcoTitle.vue'
export { default as SharedModal } from '../../components/shared/Modal.vue'
export { default as SharedSelecter } from '../../components/shared/Selecter.vue'
export { default as SharedTag } from '../../components/shared/Tag.vue'
export { default as SharedTitleBig } from '../../components/shared/TitleBig.vue'
export { default as SharedTitleMedium } from '../../components/shared/TitleMedium.vue'
export { default as SharedTitleSmall } from '../../components/shared/TitleSmall.vue'
export { default as SharedTypeStorageFilter } from '../../components/shared/TypeStorageFilter.vue'
export { default as SharedSectionlanding2 } from '../../components/shared/sectionlanding2.vue'
export { default as SharedPicker } from '../../components/shared/picker/index.js'
export { default as SharedPickerWrapper } from '../../components/shared/picker/wrapper.js'
export { default as SharedPickerComponentsVuePicker } from '../../components/shared/picker/components/VuePicker.vue'
export { default as SharedPickerComponentsVuePickerOption } from '../../components/shared/picker/components/VuePickerOption.vue'
export { default as SharedPickerMixinsAttrs } from '../../components/shared/picker/mixins/attrs.js'
export { default as SharedPickerMixinsDropdownControls } from '../../components/shared/picker/mixins/dropdown-controls.js'
export { default as SharedPickerMixinsKeyControls } from '../../components/shared/picker/mixins/key-controls.js'
export { default as SharedPickerHelpersOuterClick } from '../../components/shared/picker/helpers/outer-click.js'

export const LazyFooter = import('../../components/Footer.vue' /* webpackChunkName: "components/footer" */).then(c => wrapFunctional(c.default || c))
export const LazyNavbar = import('../../components/Navbar.vue' /* webpackChunkName: "components/navbar" */).then(c => wrapFunctional(c.default || c))
export const LazyPartnersHowItWork = import('../../components/partners/HowItWork.vue' /* webpackChunkName: "components/partners-how-it-work" */).then(c => wrapFunctional(c.default || c))
export const LazyPartnersHowItWorkVar = import('../../components/partners/HowItWorkVar.vue' /* webpackChunkName: "components/partners-how-it-work-var" */).then(c => wrapFunctional(c.default || c))
export const LazyStoragesCardEdit = import('../../components/storages/CardEdit.vue' /* webpackChunkName: "components/storages-card-edit" */).then(c => wrapFunctional(c.default || c))
export const LazyStoragesCardOrder = import('../../components/storages/CardOrder.vue' /* webpackChunkName: "components/storages-card-order" */).then(c => wrapFunctional(c.default || c))
export const LazyStoragesSearchResultItem = import('../../components/storages/SearchResultItem.vue' /* webpackChunkName: "components/storages-search-result-item" */).then(c => wrapFunctional(c.default || c))
export const LazySharedAccount = import('../../components/shared/Account.vue' /* webpackChunkName: "components/shared-account" */).then(c => wrapFunctional(c.default || c))
export const LazySharedAddingFile = import('../../components/shared/AddingFile.vue' /* webpackChunkName: "components/shared-adding-file" */).then(c => wrapFunctional(c.default || c))
export const LazySharedCheckbox = import('../../components/shared/Checkbox.vue' /* webpackChunkName: "components/shared-checkbox" */).then(c => wrapFunctional(c.default || c))
export const LazySharedCoreArea = import('../../components/shared/CoreArea.vue' /* webpackChunkName: "components/shared-core-area" */).then(c => wrapFunctional(c.default || c))
export const LazySharedCoreButton = import('../../components/shared/CoreButton.vue' /* webpackChunkName: "components/shared-core-button" */).then(c => wrapFunctional(c.default || c))
export const LazySharedCoreCheckbox = import('../../components/shared/CoreCheckbox.vue' /* webpackChunkName: "components/shared-core-checkbox" */).then(c => wrapFunctional(c.default || c))
export const LazySharedCoreInput = import('../../components/shared/CoreInput.vue' /* webpackChunkName: "components/shared-core-input" */).then(c => wrapFunctional(c.default || c))
export const LazySharedDefaultArea = import('../../components/shared/DefaultArea.vue' /* webpackChunkName: "components/shared-default-area" */).then(c => wrapFunctional(c.default || c))
export const LazySharedDefaultButton = import('../../components/shared/DefaultButton.vue' /* webpackChunkName: "components/shared-default-button" */).then(c => wrapFunctional(c.default || c))
export const LazySharedDefaultInput = import('../../components/shared/DefaultInput.vue' /* webpackChunkName: "components/shared-default-input" */).then(c => wrapFunctional(c.default || c))
export const LazySharedDropDownFilter = import('../../components/shared/DropDownFilter.vue' /* webpackChunkName: "components/shared-drop-down-filter" */).then(c => wrapFunctional(c.default || c))
export const LazySharedIcoTitle = import('../../components/shared/IcoTitle.vue' /* webpackChunkName: "components/shared-ico-title" */).then(c => wrapFunctional(c.default || c))
export const LazySharedModal = import('../../components/shared/Modal.vue' /* webpackChunkName: "components/shared-modal" */).then(c => wrapFunctional(c.default || c))
export const LazySharedSelecter = import('../../components/shared/Selecter.vue' /* webpackChunkName: "components/shared-selecter" */).then(c => wrapFunctional(c.default || c))
export const LazySharedTag = import('../../components/shared/Tag.vue' /* webpackChunkName: "components/shared-tag" */).then(c => wrapFunctional(c.default || c))
export const LazySharedTitleBig = import('../../components/shared/TitleBig.vue' /* webpackChunkName: "components/shared-title-big" */).then(c => wrapFunctional(c.default || c))
export const LazySharedTitleMedium = import('../../components/shared/TitleMedium.vue' /* webpackChunkName: "components/shared-title-medium" */).then(c => wrapFunctional(c.default || c))
export const LazySharedTitleSmall = import('../../components/shared/TitleSmall.vue' /* webpackChunkName: "components/shared-title-small" */).then(c => wrapFunctional(c.default || c))
export const LazySharedTypeStorageFilter = import('../../components/shared/TypeStorageFilter.vue' /* webpackChunkName: "components/shared-type-storage-filter" */).then(c => wrapFunctional(c.default || c))
export const LazySharedSectionlanding2 = import('../../components/shared/sectionlanding2.vue' /* webpackChunkName: "components/shared-sectionlanding2" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPicker = import('../../components/shared/picker/index.js' /* webpackChunkName: "components/shared-picker" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerWrapper = import('../../components/shared/picker/wrapper.js' /* webpackChunkName: "components/shared-picker-wrapper" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerComponentsVuePicker = import('../../components/shared/picker/components/VuePicker.vue' /* webpackChunkName: "components/shared-picker-components-vue-picker" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerComponentsVuePickerOption = import('../../components/shared/picker/components/VuePickerOption.vue' /* webpackChunkName: "components/shared-picker-components-vue-picker-option" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerMixinsAttrs = import('../../components/shared/picker/mixins/attrs.js' /* webpackChunkName: "components/shared-picker-mixins-attrs" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerMixinsDropdownControls = import('../../components/shared/picker/mixins/dropdown-controls.js' /* webpackChunkName: "components/shared-picker-mixins-dropdown-controls" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerMixinsKeyControls = import('../../components/shared/picker/mixins/key-controls.js' /* webpackChunkName: "components/shared-picker-mixins-key-controls" */).then(c => wrapFunctional(c.default || c))
export const LazySharedPickerHelpersOuterClick = import('../../components/shared/picker/helpers/outer-click.js' /* webpackChunkName: "components/shared-picker-helpers-outer-click" */).then(c => wrapFunctional(c.default || c))
