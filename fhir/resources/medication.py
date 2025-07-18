from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Medication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of a Medication.
    This resource is primarily used for the identification and definition of a
    medication, including ingredients, for the purposes of prescribing,
    dispensing, and administering a medication as well as for making statements
    about medication use.
    """

    __resource_type__ = "Medication"

    batch: fhirtypes.MedicationBatchType | None = Field(  # type: ignore
        default=None,
        alias="batch",
        title="Details about packaged medications",
        description="Information that only applies to packages (not products).",
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="code",
        title="Codes that identify this medication",
        description=(
            "A code (or set of codes) that specify this medication, or a textual "
            "description if no code is available. Usage note: This could be a "
            "standard medication code such as a code from RxNorm, SNOMED CT, IDMP "
            "etc. It could also be a national or local formulary code, optionally "
            "with translations to other code systems."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    definition: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="definition",
        title="Knowledge about this medication",
        description=(
            "A reference to a knowledge resource that provides more information "
            "about this medication."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MedicationKnowledge"],
        },
    )

    doseForm: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="doseForm",
        title="powder | tablets | capsule +",
        description="Describes the form of the item.  Powder; tablets; capsule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="Business identifier for this medication",
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.MedicationIngredientType] | None = Field(  # type: ignore
        default=None,
        alias="ingredient",
        title="Active or inactive ingredient",
        description="Identifies a particular constituent of interest in the product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    marketingAuthorizationHolder: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="marketingAuthorizationHolder",
        title="Organization that has authorization to market medication",
        description=(
            "The company or other legal entity that has authorization, from the "
            "appropriate drug regulatory authority,  to market a medicine in one or"
            " more jurisdictions.  Typically abbreviated MAH.Note:  The MAH may "
            "manufacture the product and may also contract the manufacturing of the"
            " product to one or more companies (organizations)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the medication is in active use.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    totalVolume: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="totalVolume",
        title=(
            "When the specified product code does not infer a package size, this is"
            " the specific amount of drug in the product"
        ),
        description=(
            "When the specified product code does not infer a package size, this is"
            " the specific amount of drug in the product.  For example, when "
            "specifying a product that has the same strength (For example, Insulin "
            "glargine 100 unit per mL solution for injection), this attribute "
            "provides additional clarification of the package amount (For example, "
            "3 mL, 10mL, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``Medication`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "code",
            "status",
            "marketingAuthorizationHolder",
            "doseForm",
            "totalVolume",
            "ingredient",
            "batch",
            "definition",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``Medication`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "modifierExtension",
            "identifier",
            "code",
            "status",
            "marketingAuthorizationHolder",
            "totalVolume",
        ]


class MedicationBatch(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details about packaged medications.
    Information that only applies to packages (not products).
    """

    __resource_type__ = "MedicationBatch"

    expirationDate: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="expirationDate",
        title="When batch will expire",
        description="When this specific batch of product will expire.",
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_expirationDate",
        title="Extension field for ``expirationDate``.",
    )

    lotNumber: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="lotNumber",
        title="Identifier assigned to batch",
        description="The assigned lot number of a batch of the specified product.",
        json_schema_extra={
            "element_property": True,
        },
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MedicationBatch`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "lotNumber", "expirationDate"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MedicationBatch`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class MedicationIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """

    __resource_type__ = "MedicationIngredient"

    isActive: bool | None = Field(  # type: ignore
        default=None,
        alias="isActive",
        title="Active ingredient indicator",
        description=(
            "Indication of whether this ingredient affects the therapeutic action "
            "of the drug."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_isActive", title="Extension field for ``isActive``."
    )

    item: fhirtypes.CodeableReferenceType = Field(  # type: ignore
        default=...,
        alias="item",
        title=(
            "The ingredient (substance or medication) that the ingredient.strength "
            "relates to"
        ),
        description=(
            "The ingredient (substance or medication) that the ingredient.strength "
            "relates to.  This is represented as a concept from a code system or "
            "described in another resource (Substance or Medication)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance", "Medication"],
        },
    )

    strengthCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="strengthCodeableConcept",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": False,
        },
    )

    strengthQuantity: fhirtypes.QuantityType | None = Field(  # type: ignore
        default=None,
        alias="strengthQuantity",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": False,
        },
    )

    strengthRatio: fhirtypes.RatioType | None = Field(  # type: ignore
        default=None,
        alias="strengthRatio",
        title="Quantity of ingredient present",
        description=(
            "Specifies how many (or how much) of the items there are in this "
            "Medication.  For example, 250 mg per tablet.  This is expressed as a "
            "ratio where the numerator is 250mg and the denominator is 1 tablet but"
            " can also be expressed a quantity when the denominator is assumed to "
            "be 1 tablet."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e strength[x]
            "one_of_many": "strength",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``MedicationIngredient`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "item",
            "isActive",
            "strengthRatio",
            "strengthCodeableConcept",
            "strengthQuantity",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``MedicationIngredient`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "strength": ["strengthCodeableConcept", "strengthQuantity", "strengthRatio"]
        }
        return one_of_many_fields
